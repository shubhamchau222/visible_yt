import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__verision__ = "0.0.0"
REPO_NAME = "visible_yt"
AUTHOR_USER_NAME = "shubhamchau222"
SRC_REPO = "visible_yt"
AUTHOR_EMAIL = "shubhamchau78@gmail.com"

setuptools.setup(

    name= SRC_REPO,
    version= __verision__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package to see YT Videos",
    long_description= long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)