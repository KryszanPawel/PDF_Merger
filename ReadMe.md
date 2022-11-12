<h1>PDF Merger</h1>
<hr>

<p>Merger app is an answer to my need at work to combine multiple pdfs together.</p>
<img src="./Screenshots/UI.png">
<p>PDF Merger can join up to 6 files.</p>
<p>If user choose pdf file, document is added to list.</p>
<img src="./Screenshots/add.png">
<p>In case of choosing different extension alert is raised.</p>
<img src="./Screenshots/6_pdfs.png">
<p>If mistake was made during creating list of files to merge, <br>list can be cleared using "Clear List" button.</p>

<p>Application expects user to choose target path for merged file.</p>
<img src="./Screenshots/path.png">
<p>If user will not specify it, merged file will be saved in application root directory.</p>
<hr>
<h3>Used resources</h3>
<hr>
<p>Application GUI is built on tkinter with small assist of Pillow. <br> Main functionality is achieved
with PyPDF2.</p>