# rcc-user-guide
The User Guide for The University of Chicago's Research Computing Center's High Performance Computing Clusters.

content from current site: https://projects.rcc.uchicago.edu/rcc/midway2/site/   

**How to make a suggestion or report an error (fastest way)**  
Click the [Issues](https://github.com/rcc-uchicago/user-guide/issues) tab in this repository, and create a [New Issue](https://github.com/rcc-uchicago/user-guide/issues/new)


**How to edit User Guide content**

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and then clone this repository  

2. Install Material for MkDocs  
Run the following line in your command line interface (terminal/powershell)  
    ```
    pip install mkdocs-material
    ```

3. Build the site locally  
Enter the location of the cloned fork
    ```
    cd <repo_folder>
    ```

    Then run:  
    ```
    mkdocs serve
    ```
    mkdocs will open up its built-in dev server that lets you preview documentation as you work on it. Simply open the provided address (something like: http://127.0.0.1:8000/) in your browser of choice, and you should see the user guide. As you make changes to the source documents, this  site will automatically update.  For more information, see [here](https://www.mkdocs.org/getting-started/).  

4. Edit content  
Make whatever edits or additions to the user guide by editing the source markdown documents, located in `docs/`. 
5. Update `mkdocs.yml`  
If you add any new pages or change any page names, be sure to update the `nav` section in `mkdocs.yml`, and check the dev server to ensure the updated `nav` is working.

6. Submit a pull request  
When you've made your changes, submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) and they will be reviewed before merging with the base branch.