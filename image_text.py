from PIL import Image
import pytesseract
import re

path = "/Users/yayun/Downloads/IMG_3385.jpg"
dict = {
    "flax": "flax",
    "cotton": "cotton",
    "coton": "cotton",
    "wool": "wool",
    "viscose": "viscose",
    "polypropylene": "polypropylene",
    "polyester": "polyester",
    "acrylic": "acrylic",
    "nylon": "nylon",
    "hemp": "hemp",
}


pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"


def process_image(iamge_name, lang_code="eng"):
    return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)


def extract_textile(raw_text, textile_dict):
    fabric = {}
    raw_list = raw_text.lower().split("\n")
    for i in range(len(raw_list)):
        for j in textile_dict.keys():
            if j in raw_list[i]:
                pattern = r"[0-9]{1,3}(?=%)"
                percentage = int(re.findall(pattern, raw_list[i])[0])
                fabric[textile_dict[j]] = percentage
                # if the total percentage equal to 100, end the search
                if sum(fabric.values()) == 100:
                    return fabric
                else:
                    break
            else:
                continue
    if sum(fabric.values()) != 100:
        return f"take a picture of the label again"
    else:
        return fabric


def main(image_path, textile_dict):
    data_eng = process_image(image_path)
    dic = extract_textile(data_eng, textile_dict)
    return


if __name__ == "__main__":
    main(path, dict)
