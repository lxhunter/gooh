import yaml
import sh
from urlparse import urlparse
from os.path import splitext, basename, exists
from os import makedirs
from semantic_version import Version, Spec, validate


#class Update(object):

def update(args):
    dependency_file = args.dependency_file
    clone_path = args.clone_path

    requirements = []

    with open(dependency_file, 'r') as stream:
        try:
            requirements = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    git = sh.git.bake(_cwd=clone_path)

    if not exists(clone_path):
        makedirs(clone_path)

    for requirement in requirements:
        if 'src' not in requirement:
            print 'no src found'
            break
        else:
            src = requirement['src']

        if 'name' in requirement:
            name = requirement['name']
        else:
            disassembled = urlparse(requirement['src'])
            name, _ = splitext(basename(disassembled.path))

        branch = 'master'
        version = None

        if 'version' in requirement:
            version = requirement['version']

        if 'branch' in requirement:
            branch = requirement['branch']

        repo = sh.git.bake(_cwd=clone_path + '/' + name)

        if not exists(clone_path + '/' + name):
            print 'Cloning: ' + name + ' into ' + clone_path + '/' + name
            git.clone(src, name)
        else:
            print 'Pulling: ' + name + ' into ' + clone_path + '/' + name
            repo.checkout(branch)

        repo.pull('--tags')

        versions = []

        for tag in repo.tag('-l').split('\n'):
            if tag and validate(tag):
                versions.append(Version(tag))

        if version:
            spec = Spec(version)
            selected_version = spec.select(versions)
            if selected_version is None:
                print 'No suitable version: ' + version + ' found for ' + name + ' in ' + str(versions)
                exit(1)
            print 'Selecting version: ' + str(selected_version) + ' for ' + name + ' from ' + str(versions)
            repo.checkout('tags/' + str(selected_version))
