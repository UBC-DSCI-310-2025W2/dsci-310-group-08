# Predicting Park Access Rankings Across U.S. Cities :national_park:
**Authors**: Jingyuan Liu, Shivani Aggarwal, Sarenna Ulman, Luna Gulec

## About

## Report
The report of this project can be found [here](notebooks/parks_analysis.ipynb).
## Innstructions
**We use a Docker container image to make the computational environment reproducible for this project. You can interactively run, edit, and explore the project in Jupyter Lab by following the instructions below.**\
*Please ignore the first two steps if you already have Docker set up.*
- You will use Docker to recreate the computational environment for this analysis. For this, you will need a Docker account. You can sign up for a free one [here](https://app.docker.com/accounts/ljy0401).
- After signing up and signing into the Docker Store, go [here](https://docs.docker.com/desktop/setup/install/windows-install/) and click on the “Get Docker Desktop” button on the right-hand side of the screen. Then follow the installation instructions on that screen to install the stable version.
- Open your terminal and navigate to the project's root directory using the `cd` command.
- Make sure your Docker is running.
- Run the following command to start the environment: `docker-compose up`.
- Once the container has launched, users need to navigate to a web browser (i.e., Chrome) and copy the URL `http://localhost:8888/lab` into their web browser to access Jupyter Lab.
- Enter `dsci310_group_08` as the token/password to log into Jupyter Lab.
- Next, in Jupyter Lab, navigate to the `/work` folder, you should be able to see all files and folders in our project repo there.
- Open `/notebooks/parks_analysis.ipynb` and click **Kernel** > **Restart and runall** to run the entire analysis.
- Once you are done, <kbd>CTRL</kbd>+<kbd>C</kbd> to stop and clean up the launched container.
- Then type `docker-compose down` in the terminal.
## Dependencies
Python 3.13.11, Jupyter and Python Packages listed in the default scipy notebook base Docker image [here](https://github.com/jupyter/docker-stacks/wiki/x86_64-default-scipy-notebook-0dd81e2dd718).
## Licenses
This project report is offered under 
the [Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
The code and software provided in this project are offered under the [MIT open source license](https://opensource.org/licenses/MIT). See [the license file](LICENSE.md) for more information. 
