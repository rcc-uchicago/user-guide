# rcc-user-guide
The User Guide for The University of Chicago's Research Computing Center's High Performance Computing Clusters.

content from current site: https://projects.rcc.uchicago.edu/rcc/midway2/site/   

**How to make a suggestion or report an error (fastest way)**  
Click the [Issues](https://github.com/rcc-uchicago/user-guide/issues) tab in this repository, and create a [New Issue](https://github.com/rcc-uchicago/user-guide/issues/new)


**How to edit User Guide content**

1. Install Material for MkDocs
Run the following line in your command line interface (terminal/powershell)  
    ```
    pip install mkdocs-material
    ```
This installation step is only required if mkdocs has not been installed on your machine.

2. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and/or clone this repository into your space
   ```
   git clone https://github.com/rcc-uchicago/user-guide.git rcc-user-guide
   ```

3. Build the site locally  
Enter the location of the cloned fork (`user-guide`), and create a new branch for your edits
    ```
    cd user-guide
    git checkout -b my-edits
    ```

    Then run:
    ```
    mkdocs serve
    ```

    mkdocs will open up its built-in dev server that lets you preview documentation as you work on it. Simply open the provided address (something like: http://127.0.0.1:8000/) in your browser of choice, and you should see the user guide. As you make changes to the source documents, this  site will automatically update.  For more information, see [here](https://www.mkdocs.org/getting-started/).  

4. Edit content
Make whatever edits or additions to the user guide by editing the source markdown documents, located in `docs/`. (Editable canva infographics: [RCC Workflow](https://www.canva.com/design/DAFQE3SCdzw/66GWBkbNEc6RApV25ZTeVQ/edit?utm_content=DAFQE3SCdzw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton), [Running Jobs Workflow](https://www.canva.com/design/DAFQom0o07g/YnCNw4zYkjFogxGr1dPZSw/edit?utm_content=DAFQom0o07g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton), [Midway2 Storage](https://www.canva.com/design/DAFQJ5BoJnE/hFVtpc8QI84bAzIrBkJ-Bw/edit?utm_content=DAFQJ5BoJnE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton), and [Midway3 Storage](https://www.canva.com/design/DAFQKdiiwPE/wOZDdsaGyZOAeLQqbQxudw/edit?utm_content=DAFQKdiiwPE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).


5. Update `mkdocs.yml`
If you add any new pages or change any page names, be sure to update the `nav` section in `mkdocs.yml`, and check the dev server to ensure the updated `nav` is working.

6. Submit a pull request
When you've made your changes, commit the changes you have made in your branch, push the new branch to GitHub:
    ```
    git add [your added files, if any]
    git commit -a
    git push --set-upstream origin my-edits
    ```
