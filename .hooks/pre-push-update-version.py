import json
import subprocess

# https://habr.com/ru/companies/dins/articles/584562/

PATH_TO_JSON = "./Versioning/version.json"
PATH_TO_REPOSITORY = "./"

print("pre-push-hook: Обновление версии!")

#
#
#
#

def gitAdd(fileName):
    global PATH_TO_REPOSITORY
    cmd = ['git', 'add', fileName]
    p = subprocess.Popen(cmd, cwd=PATH_TO_REPOSITORY)
    p.wait()

def gitCommit():
    global PATH_TO_REPOSITORY
    cmd = ['git', 'commit', '-m', '"chore: Update version"']
    p = subprocess.Popen(cmd, cwd=PATH_TO_REPOSITORY)
    p.wait()

#
#
#
#

with open(PATH_TO_JSON, 'r') as openfile:
    json_object = json.load(openfile)

current_version = float(json_object['version'])
new_version = current_version + 0.01

json_object['version'] = new_version

with open(PATH_TO_JSON, "w") as outfile:
    json.dump(json_object, outfile)

gitAdd(PATH_TO_JSON)
gitCommit()
