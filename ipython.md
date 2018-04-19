# IPython

## How to create a kernel for a different environment
`python -m ipykernel install --user --name <environment name> --display-name "<kernel name>"`
    - https://github.com/palpen/udacity_ml_engineer_projects/tree/master/dog-project
    - http://ipython.readthedocs.io/en/stable/install/kernel_install.html

## Create a cell with a button that toggles viewing of code cells
Add this to the first cell in your notebook ([source](http://blog.nextgenetics.net/?e=102)). Clicking the link will hide/show cells containing code.

```python
from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
The raw code for this IPython notebook is by default hidden for easier reading.
To toggle on/off the raw code, click <a href="javascript:code_toggle()">here</a>.''')
```
