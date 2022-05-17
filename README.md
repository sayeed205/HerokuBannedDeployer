# HerokuBannedDeployer

### IT IS MANDITORY TO FORK THIS REPO

With this you can deploy repos that are banned/blacklisted by heroku in different platforms

# Deploy From Here

## Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Frahulps1000%2FHerokuBannedDeployer&envs=REPO_URL%2CPYTHON_FILE%2COTHER_INSTALLS&optionalEnvs=OTHER_INSTALLS&REPO_URLDesc=URL+of+the+REPO+that+you+want+to+deploy.&PYTHON_FILEDesc=Name+of+the+python+file+that+you+need+to+run.+%5Buse+-m+if+you+need+to+run+__main__.py+from+a+folder%5D&OTHER_INSTALLSDesc=If+you+need+install+packages+for+running+your+app%28Python+is+pre-installed%29.%5BSpace+in+between+each+package%5D&OTHER_INSTALLSDefault=None)
<br>

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Note:

### If you are deploying mirror bot then import this repo and make the repo private. Upload your tocke,pickle to the private repo then deploy. If you are using service account then upload the accounts folder to the private repo then deploy. \ For `config.env` use [GitHub Gist](https://gist.github.com) and use the raw file use link without commit code in `CONFIG_FILE_URL` as heroku var. Same goes for `drive_folder`.

## Setup `CONFIG_FILE_URL`

![Steps 1 to 3](https://i.imgur.com/hKJ71gW.png)
Go to [GitHub Gist](gist.github.com) set name as config.env and fill all variables.
![Step 4](https://i.imgur.com/2VA4WK5.png)
After creating gist file click raw button.
![Step 5](https://i.imgur.com/c6anvBd.png)

Remove commit id from raw link to be able to change variables without updating the CONFIG_FILE_URL in secrets. Should be in this form: https://gist.githubusercontent.com/username/gist-id/raw/config.env

- Before: https://gist.githubusercontent.com/anasty17/8cce4a4b4e7f4ea47e948b2d058e52ac/raw/19ba5ab5eb43016422193319f28bc3c7dfb60f25/config.env
- After: https://gist.githubusercontent.com/anasty17/8cce4a4b4e7f4ea47e948b2d058e52ac/raw/config.env

After copying the raw gist link set it to heroku variable.
