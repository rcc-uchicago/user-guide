
![UChicago_Research_Computing-Center_Horizontal_Color-RGB](https://user-images.githubusercontent.com/53494838/211921211-67560837-60de-4196-b3e1-baadb559315e.png)
<p align="center">
 <strong>
 User Guide for the
 <a href="https://rcc.uchicago.edu/">UChicago Research Computing Center's</a> 
 High Performance Computing Clusters
</strong>
</p>

<p align="center">
View the docs: https://rcc-uchicago.github.io/user-guide/
</p>

<p align="center">
Make a suggestion or report an issue: https://github.com/rcc-uchicago/user-guide/issues/new
</p>


<h2></h2>

**Edit the guide yourself**

1. Install Material for MkDocs
    Run the following line in your command line interface (terminal/powershell):  
    ```
    pip install mkdocs-material
    ```
    If already installed, update for latest functionality:
    ```
    pip install --upgrade mkdocs-material
    ```

2. Clone this repository to your machine. 
   ```
   git clone https://github.com/rcc-uchicago/user-guide.git rcc-user-guide
   ```

3. Build the site locally  
   Enter the repository (`rcc-user-guide`) and create a new branch for your edits
    ```
    cd rcc-user-guide
    git checkout -b my-edits
    ```

    Then run:
    ```
    mkdocs serve
    ```

    mkdocs will open up its built-in dev server that lets you preview documentation as you work on it. Simply open the provided address (something like: http://127.0.0.1:8000/) in your browser of choice, and you should see the user guide. As you make changes to the source documents, this  site will automatically update.  For more information, see [here](https://www.mkdocs.org/getting-started/).  

    If there are messages about missing modules, e.g. `monorepo`, install them
    ```
    pip install mkdocs-monorepo-material
    ```

4. Edit content  
Make whatever edits or additions to the user guide by editing the source markdown documents, located in `docs/`. (Editable canva infographics: [RCC Workflow](https://www.canva.com/design/DAFQE3SCdzw/66GWBkbNEc6RApV25ZTeVQ/edit?utm_content=DAFQE3SCdzw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton), [Running Jobs Workflow](https://www.canva.com/design/DAFQom0o07g/YnCNw4zYkjFogxGr1dPZSw/edit?utm_content=DAFQom0o07g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)).


5. Update `mkdocs.yml`  
If you add any new pages or change any page names, be sure to update the `nav` section in `mkdocs.yml`, and check the dev server to ensure the updated `nav` is working.

6. Submit a pull request  
When you've made your changes, commit the changes you have made in your branch, push the new branch to GitHub:
    ```
    git add [your added files, if any]
    git commit -a
    git push --set-upstream origin my-edits
    ```
