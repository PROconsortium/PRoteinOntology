

//Progress Bar script- by Todd King (tking@igpp.ucla.edu)
//Modified by JavaScript Kit for NS6, ability to specify duration
//Visit JavaScript Kit (http://javascriptkit.com) for script

var duration=3 // Specify duration of progress bar in seconds
var _progressWidth = 50;	// Display width of progress bar

var _progressBar = new String("");
var _progressEnd = 10;
var _progressAt = 0;


// Create and display the progress dialog.
// end: The number of steps to completion
function ProgressCreate(end) {
	// Initialize state variables
	_progressEnd = end;
	_progressAt = 0;

	// Move layer to center of window to show
	if (document.all) {	// Internet Explorer
		progress.className = 'show2';
		progress.style.left = (document.body.clientWidth/2) - (progress.offsetWidth/2);
		progress.style.top = document.body.scrollTop+(document.body.clientHeight/2) - (progress.offsetHeight/2);
	} else if (document.layers) {	// Netscape
		document.progress.visibility = true;
		document.progress.left = (window.innerWidth/2) - 100;
		document.progress.top = pageYOffset+(window.innerHeight/2) - 40;
	} else if (document.getElementById) {	// Netscape 6+
		document.getElementById("progress").className = 'show2';
		document.getElementById("progress").style.left = (window.innerWidth/2)- 100;
		document.getElementById("progress").style.top = pageYOffset+(window.innerHeight/2) - 40;
	}

	ProgressUpdate();	// Initialize bar
}

// Hide the progress layer
function ProgressDestroy() {
	// Move off screen to hide
	if (document.all) {	// Internet Explorer
		progress.className = 'hide2';
	} else if (document.layers) {	// Netscape
		document.progress.visibility = false;
	} else if (document.getElementById) {	// Netscape 6+
		document.getElementById("progress").className = 'hide2';
	}
}

// Increment the progress dialog one step
function ProgressStepIt() {
	_progressAt++;
	if(_progressAt > _progressEnd*5) _progressAt = _progressAt % _progressEnd;
	ProgressUpdate();
}

// Update the progress dialog with the current state
function ProgressUpdate() {
	var n = (_progressWidth / _progressEnd) * _progressAt/6;
	if (document.all) {	// Internet Explorer
		var bar = dialog.bar;
 	} else if (document.layers) {	// Netscape
		var bar = document.layers["progress"].document.forms["dialog"].bar;
		n = n * 0.55;	// characters are larger
	} else if (document.getElementById){
                var bar=document.dialog.bar
        }
	var temp = _progressBar.substring(0, n);
	bar.value = temp;
}

// Demonstrate a use of the progress dialog.
function Demo() {
	ProgressCreate(10);
	window.setTimeout("Click()", 100);
}

function Click() {
	if(_progressAt >= _progressEnd) {
	//	ProgressDestroy();
	//	return;
	}
	ProgressStepIt();
	window.setTimeout("Click()", (duration-1)*10000/10);
}

function CallJS(jsStr) { //v2.0
  return eval(jsStr)
}

  document.write("<span id=\"progress\" class=\"hide2\">");
	document.write("<FORM name=dialog>");
	document.write("<TABLE width=220 height=70 border=4 cellpadding=0 cellspacing=0 align=center bgcolor='#FFFFFF' >");
	document.write("<TR><TD ALIGN=\"center\"> ");
	document.write("Processing ... <BR>");
	document.write("<input type=text name=\"bar\" size=\"" + _progressWidth/2 + "\"");
	if(document.all||document.getElementById) 	// Microsoft, NS6
		document.write(" bar.style=\"color:navy;\">");
	else	// Netscape
		document.write("> ");
	document.write("<br></TD></TR>");
	document.write("</TABLE>");
	document.write("</FORM>");
  document.write("</span>");
  ProgressDestroy();	// Hides



