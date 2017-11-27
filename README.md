# Pylot

A Kubernetes deploy tool

## Purpose

Pylot is a prototype exploring ways to provide a more user-friendly way to deploy kubernetes applications.

The main design goals are:
 
1) to incorporate typing using the client-python Swagger specs, to make writing specs as IDE-friendly as possible
2) to wrap and/or hide the complexity of client-python's Swagger types if/where possible
3) to enable the specification of nontrivial scripted deployment flows in Python, such as canary or green-blue deploys.

## Getting started

### Installing

First install pylot. Currently this project is not hosted on PyPi, so clone the repo and egg-install it:

```bash
git clone git@github.com:paultiplady/pylot.git
cd pylot
pip install -e .
```

### Configuration

The `Configuration` class specifies config values that are to be injected into the application.
 
```python
class MyConfig(Configuration):
    foo = Field()
    bar = Field(default='BAR')
```

### Job

The `Job` class encapsulates a deploy job, binding a Configuration to a set of Kubernetes API objects.

At runtime the configuration values will be injected into the Job, producing the final specs to be created.

```python
my_job = Job(
    configuration_cls=MyConfig,
    objects=[V1Pod()],
)
```

### Deploying

After specifying a job, it can be run like so:

```bash
pylot deploy --dry-run package.job_module
```

Note that the string `package.job_module` refers to the package containing the Job to be run, which must be on the Python path.
