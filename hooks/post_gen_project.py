def git_init():
    import subprocess

    try:
        # Run git init .
        subprocess.run(['git', 'init', '.'], check=True)
        subprocess.run(['make', 'git-config-local'], check=True)
        print("Git repository initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def make_first_commit():
    import subprocess

    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
        print("First commit successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def make_dev():
    import subprocess

    try:
        subprocess.run(['make', 'dev'], check=True)
        print("Make dev successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def remove_file(filepath):
    import os

    dir = os.path.realpath(os.path.curdir)
    os.remove(os.path.join(dir, filepath))


if __name__ == '__main__':
    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if {{ cookiecutter.init_git }}:
        git_init()
        make_first_commit()

    make_dev()
