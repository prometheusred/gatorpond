from fabric import task
import os

# Default compose files
CORE_COMPOSE = "docker-compose.gatorpond.yml"
DEV_COMPOSE = "docker-compose.gatorpond.dev.yml"
OBS_COMPOSE = "docker-compose.observability.yml"
OVERRIDE_COMPOSE = "docker-compose.override.yml"

@task
def check_versions(c):
    """
    Print versions of Python, Fabric, and Podman Compose.
    """
    c.run("python --version")
    c.run("pip freeze | grep fabric", warn=True)
    c.run("podman-compose --version", warn=True)

@task
def init_dev(c):
    """
    Install dev dependencies into current environment.
    Assumes .venv is already created.
    """
    print("Installing dev dependencies into current environment...")
    c.run("pip install --upgrade pip", pty=True)
    c.run("pip install -r dev-requirements.txt", pty=True)
    print("Done. Run:")
    print("  source .venv/bin/activate")
    print("  fab dev")

@task
def dev(c):
    """
    Run local dev with hot-reloaded user code.
    """
    c.run(
        f"podman-compose -f {DEV_COMPOSE} up --build",
        pty=True,
    )

@task
def dev_down(c):
    """
    Stop and remove all dev containers.
    """
    c.run(
        f"podman-compose -f {DEV_COMPOSE} down",
        pty=True,
    )

@task
def dev_obs(c):
    """
    Run local dev with observability stack.
    """
    c.run(
        f"podman-compose -f {CORE_COMPOSE} -f {OVERRIDE_COMPOSE} -f {OBS_COMPOSE} up --build",
        pty=True,
    )

@task
def deploy(c):
    """
    Run production build locally (no override).
    """
    c.run(
        f"podman-compose -f {CORE_COMPOSE} up --build",
        pty=True,
    )

@task
def deploy_obs(c):
    """
    Run production build with observability.
    """
    c.run(
        f"podman-compose -f {CORE_COMPOSE} -f {OBS_COMPOSE} up --build",
        pty=True,
    )

@task
def down(c):
    """
    Stop and remove all containers.
    """
    c.run(
        f"podman-compose -f {CORE_COMPOSE} -f {OVERRIDE_COMPOSE} -f {OBS_COMPOSE} down",
        pty=True,
    )

@task
def remote_deploy(c):
    """
    Placeholder for future remote deployment logic.
    """
    print("Remote deploy placeholder. Configure this for actual deployment later.")

@task
def bootstrap_dagster(c):
    """
    Placeholder for initializing Dagster metadata DB, migrations, etc.
    """
    print("Bootstrap placeholder. You can add init scripts here later.")
