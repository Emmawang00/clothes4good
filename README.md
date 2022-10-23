[![CI](https://github.com/nogibjj/mlops-template/actions/workflows/cicd.yml/badge.svg?branch=GPU)](https://github.com/nogibjj/mlops-template/actions/workflows/cicd.yml)
[![Codespaces Prebuilds](https://github.com/nogibjj/mlops-template/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg?branch=GPU)](https://github.com/nogibjj/mlops-template/actions/workflows/codespaces/create_codespaces_prebuilds)

## Clothes For Good

#### Project Goal
The web app, Clothes4Good adopts a image-to-text techinique that allows users to quickly access the footprint information of the clothes by easily scanning their clothing label. The project aims to raise people awareness toward the Earth with the hope that consumers would think twice for the goods they are buying when they see the amount of waste they could've saved. 

You may wonder what is the relationship between clothing and water waste, in fact, the textile and apparel industry is one of the largest consumers of water in manufacturing given the textile wet-processing. 

![cover picture](https://github.com/nogibjj/clothes4good/issues/1#issue-1419827715)


#### Project Flow
1. (Automatically) Devcontainter files will use Makefile, and requirements.txt to configure the workspace.
2. Image-to-Text technique enacted, we adopt `tesseract` packages.
3. Calculations for cloth material cost, i.e. energy, CO2, water, with respect to the clothing type   (e.g. dress, T-shirts) and clothing size (e.g. Small, Medium).
4. Web App Build-up by using `Streamlit`.
5. (Deploy) The Streamlit web app will be deployed on `Heruko` web service.
6. Report Generations with charts and interactive sentences based on user input!

#### Deployment in Real Life, Try it!

[Clothes4Good](https://clothes4good.herokuapp.com)

#### Data Source
https://oecotextiles.blog/2009/06/16/what-is-the-energy-profile-of-the-textile-industry
