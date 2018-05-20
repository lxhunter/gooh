gooh - Git out of (Dependency) Hell
==========
Gooh is supposed to be a *Language agnostic semantic versioner using git tags*

I am writing alot of ansible roles through my companies way of deploying infrastructures. As we started to use [molecule](http://http://molecule.readthedocs.io/) we could for the first time start using semantic versioning with our roles. (see [merge](https://gist.github.com/lxhunter/758e1e3041d7ec7aec3814018d781e29) and [semver](https://gist.github.com/lxhunter/9d4310462b6972a3f57b5f914543fd51)). We have a lot of different environments. Which makes it almost impossible to remember which version of what role was used in which environment. We tried to use `requirements.yml` for that, but it only works with version-pinning or branches. :( Nothing like [bundler](http://bundler.io), [npm](https://www.npmjs.com/) or [composer](https://getcomposer.org/) does with [tilde and caret](https://blog.madewithlove.be/post/tilde-and-caret-constraints/).

So I wrote `gooh`, I don't know if it is a dumb idea but something in the way how git handles tag makes it all so smooth and I do not have to worry about patch level changes in repos, which helps a lot, cuz every breaking change is kept for a conscious update.

Install
==========

```shell
pip install gooh
```

Versioning
==========

I use the excellent [semantic_versioing](https://github.com/rbarrois/python-semanticversion/) library, please see the documentation for what is possible.

Example
==========
#### 1. Create a yaml file named `gooh.yaml` like this:

```yaml
- src: https://github.com/lxhunter/versions.git
  version: '~1.0.0'
```

#### 2. Checkout gooh option:

```shell
$ gooh -h
usage: gooh [-h] [--dependency_file DEPENDENCY_FILE] [--clone_path CLONE_PATH]

Git Out Of Hell - Language agnostic semantic versioner using git tags

optional arguments:
  -h, --help            show this help message and exit
  --dependency_file DEPENDENCY_FILE
                        Config yaml which holds all dependencies
                        (default=gooh.yml)
  --clone_path CLONE_PATH
                        Path where the dependencies should be cloned
                        (default=roles)
```
#### 3. Use gooh to update/clone your dependencies

```shell
$ gooh
Pulling: versions into roles/versions
Selecting version: 1.0.3 for versions from [Version('1.0.1'), Version('1.0.2'), Version('1.0.3'), Version('1.1.0')]
```

Release
==========

A high level release workflow is described below.

1. Once you are ready to cut a new release of your project, you update the version in setup.py and create a new git 1. tag with `git tag $VERSION`.
1. Once you push the tag to GitHub with `git push --tags` a new CircleCI build is triggered.
2. You run a verification step to ensure that the git tag matches the version of my project that you added in step 1 above.
1. CircleCI performs all of your tests (you have tests right?).
1. Once all of your test pass, you create a new Python package and upload it to PyPI using twine.

Testing
==========

I don't know how to test gooh, if you have an idea, let me know :)


Quote
==========

"Whether you think you can or you think you can't, you're right."
- Henry Ford

Contribute
==========

[Tutorial](http://kbroman.github.io/github_tutorial/pages/fork.html)
