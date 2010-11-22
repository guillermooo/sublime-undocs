from fabric.api import run, cd

def deploy():
    with cd("hg/sublimehelp"):
        run("hg pull -u https://bitbucket.org/guillermooo/sublimehelp")
        run("rm build -fr")
        run("source ~/venvs/sublimehelp/bin/activate && make html")

    with cd("hg/sublimehelp/build/html"):
        run("rm ~/webapps/stdocs/* -r")
        run("cp . ~/webapps/stdocs -r")
