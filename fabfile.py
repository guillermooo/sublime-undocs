from fabric.api import run, cd, env

env.hosts = ["guillermooo@sublimetext.info"]

def deploy():
    with cd("dev/sublimedocs_multilang/es"):
        run("hg pull -u https://bitbucket.org/guillermooo/sublimehelpes")
        run("rm build -fr")
        run("source ~/venvs/sublimehelp/bin/activate && make html")

    with cd("dev/sublimedocs_multilang/es/build/html"):
        run("rm ~/webapps/stdocs/es/* -rf")
        run("cp . ~/webapps/stdocs/es -r")

    with cd("dev/sublimedocs_multilang/en"):
        run("hg pull -u https://bitbucket.org/guillermooo/sublimehelpen")
        run("rm build -fr")
        run("source ~/venvs/sublimehelp/bin/activate && make html")

    with cd("dev/sublimedocs_multilang/en/build/html"):
        run("rm ~/webapps/stdocs/en/* -rf")
        run("cp . ~/webapps/stdocs/en -r")
