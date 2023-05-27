# Template Repository for Automated Testing on GH-Action-Tester

This template repository, with its workflow and utilities, is designed to automate the testing process for each assignment and update the Firestore database with the results.

## Workflow Overview

The workflow is triggered on every push to any branch and can also be manually triggered through the GitHub interface. It checks out the code from the repository, determines the number of commits on the current branch, and if it's not the first commit, it proceeds to test the code and update Firestore with the results.

1. **Fork/Download this template repository.**

2. **Upload your test files.**

3. **Change the workflow to suit your tests:**

   - Open the GitHub workflow configuration file (.github/workflows/main.yml).
   - Edit the file to align with your project requirements.
     - This could mean updating the commands to install dependencies and changing the commands to run your tests.
   - Commit and push these changes to your GitHub repository.

4. **Test the pipeline by pushing the solution on the page:**
   - Upload your solution files on the assignment page.
   - This will trigger the workflow and you can see the workflow execution in the "Actions" tab of your GitHub repository or assignment page.

## Important Points of Workflow

1. **First commit handling:** The workflow skips running on the first commit to any branch. This is based on the assumption that the first commit is usually set up or groundwork, and does not include any testable code.

2. **Dependencies:** The workflow assumes that the project's dependencies are managed with npm, and that the tests can be run with npm test. If your project does not follow this convention, you may need to modify the workflow accordingly.

3. **Running Tests:** As part of the workflow, it automatically runs the tests that are defined and generates a report. The report is then used to update the Firestore with the results of the tests.

4. **Firestore update:** The last step of the workflow updates Firestore with the test results. This is achieved by running a Python script, db_writer.py, which should be located in the workflow_utils/ directory of your repository. This script should take two arguments: the branch name and a JSON file with the test results.

We hope this guide helps you understand and use the Assignment Workflow effectively. If you encounter any issues or have suggestions for improvements, feel free to open an issue or a pull request.
