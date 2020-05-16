var organismlist = [];
var organismnamelist = [];
//initializtion when user click go back
function goBackInitilization(){
	var x=document.getElementsByName("input_option"); 
	  for(var i=0;i<x.length;i++){  
	        if(x[i].value=='all')   {  
	            x[i].checked=true;  
	            break;  
	        }  
	    }  
}
//show the organism selected in the check box
function show_organism_checked(){
	 var x=parent.document.getElementsByName("organism_checkbox");  
	    for(var i=0;i<x.length;i++){
	    	for(var j=0;j<organismlist.length;j++){
			var values = x[i].value.split("----");
	    		//if(organismlist[j]==x[i].value){
	    		if(organismlist[j]==values[0]){
	    			x[i].checked=true;
	    			break;
	    		}
	    	}
	    }
}
//when use click the checked box,update the oranigam list
function organism_list(str){
	var strs = str.split("----"); 	
	//organismName.set(strs[0], strs[1]);
	var exist=false;
	var len=organismlist.length;
	var newlist= [];
	var namelist= [];
	var selectedStr = "";
	//alert(len);
	if(len==0)  {
		newlist.push(strs[0]);
		namelist.push(strs[1]);
	}
	for(var i=0;i<len;i++){
	//	alert("test");
		if(organismlist[i]==strs[0]){
			exist=true;
			continue;
		} 
		else {
			newlist.push(organismlist[i]);
			namelist.push(organismnamelist[i]);
		}
	}
	if(!exist&len>=1) {
		 newlist.push(strs[0]);
		namelist.push(strs[1]);
	}
	for(var i=0; i< newlist.length; i++) {
		var taxonURL = "<a href=\"http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id="+newlist[i]+"\" title=\""+namelist[i].replace(/\_/g, " ") +"\">"+newlist[i]+"</a>";
		var organismName = "<font color=blue>"+namelist[i].replace(/\_/g, " ")+"</font>";
		//selectedStr += taxonURL+"; ";
		selectedStr += organismName+"; ";
	}
	
	//var tmp = selectedStr;
	if(selectedStr.lastIndexOf("; ") > 0) {
		selectedStr = selectedStr.substr(0, selectedStr.lastIndexOf("; "));
	}
	
	
	//selectedStr.replace(/\;\s+\S*$/, "");
	if(newlist.length==31){
			 var x=document.getElementsByName("organism_checkbox");  
			    for(var i=0;i<x.length;i++){  
				var values = x[i].value.split("----");
			        //if(x[i].value==strs[0])  {  
			        if(values[0]==strs[0])  {  
			        	x[i].checked=false;  
			            break;  
			        }
			    }
	alert("You can select the organisms no more than 30");
	newlist.pop();	
	namelist.pop();	
	}		
	organismlist=newlist;
	organismnamelist=namelist;
	//document.getElementById("show_selected_count").innerHTML='(<b>'+organismlist.length+' selected</b>)';  
	//document.getElementById("show_selected_count").innerHTML='<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size=2><b>Selected: </b>'+selectedStr+'</font><br><br>';  
	document.getElementById("show_selected_count").innerHTML='<br><table width=850 border=0><tr style="font-size:smaller;"><td valign=top align=left width=150>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Selected ('+organismlist.length+'): </b></td><td valign=top>'+selectedStr+'</td></tr></table></font><br>';  
	}

// for the peptidesearch/batchpeptidematch.htm to handle the input
function BatchPeptideInputCheck(searchform) {	
	var keyword_value=searchform.keyword.value;
	var organism="";
	var obj = document.getElementsByName("input_option");
	for (var i=0; i<obj.length; i++){
	if (obj[i].checked){
	var	option=obj[i].value;
	break;
	}
	}
	if(option=="input"){
		if(searchform.organism_name.value.match(/^[1-9]/)==null){
		var organisms=searchform.organism_name.value.match(/\[(.*?)\]/);
		if(organisms!=null){
			organism=organisms[1];
		}
		else{
			alert("Please use the autocomplete to input the organism");
			document.getElementById('organism_name_div').style.display='inline';
			document.getElementById('organism_name').style.display='inline';
			document.getElementById('organism_name').focus();
			return (false);
		}
		}
		else organism=searchform.organism_name.value.replace(/[^0-9]+/g,'');
	}
	else if(option=="select"){
		if(organismlist.length>0){
			organism=organismlist[0];
			for(var i=1;i<organismlist.length;i++) {
			organism=organism+';'+organismlist[i];
			}
		}
		else{
		alert("Please select at least one organism");
		return (false);
		}
		
	}
	else{
		 organism="all";
	}
	if(keyword_value.length>0){
	var peptides=keyword_value.split("\n");
	var peptide=peptides[0].replace(/[^a-zA-Z]+/g,'');
	for(i=1;i<peptides.length;i++){
	 peptide=peptide+";"+peptides[i].replace(/[^a-zA-Z]+/g,'');
	}
	
	if(peptide.length<3){
		alert("Please input at least one line of 3 letters peptide");
		searchform.keyword.focus();
		return (false);
	}
	else if(organism.length==0){
		alert("Please input the valid organism");
		searchform.organism_name.focus();
		return (false);	
		}
	else{
	searchform.peptide.value=peptide;
	searchform.db.value=organism;
	alert("Starting to download");
	document.searchform.submit();
	}
	
	}
	else{
		alert("Please input at least one line of 3 letters peptide");
		searchform.keyword.focus();
		return (false);
	}
}
//for the peptidesearch/index.htm to handle the input
function PeptideInputCheck(searchform) {
	var keyword=searchform.keyword.value;
	var organism;
	var obj = document.getElementsByName("input_option");
	for (var i=0; i<obj.length; i++){
	if (obj[i].checked){
	var	option=obj[i].value;
	break;
	}
	}
	if(keyword=="*:*"){
		document.searchform.submit();
	}
	else{

	if(option=="input"){
		if(searchform.organism_name.value.match(/^[1-9]/)==null){
		var organisms=searchform.organism_name.value.match(/\[(.*?)\]/);
		if(organisms!=null){
			organism=organisms[1];
		}
		else{
			alert("Please input a valid organism name");
			document.getElementById('organism_name').style.display='inline';
			document.getElementById('organism_name_div').style.display='inline';
			document.getElementById('organism_name').focus();
			return (false);
		}
		}
			else organism=searchform.organism_name.value.replace(/[^0-9]+/g,'');
	}
	else if(option=="select"){
		if(organismlist.length>0){
			organism=organismlist[0];
			for(var i=1;i<organismlist.length;i++) {
			organism=organism+';'+organismlist[i];
			}
		}
		else{
		alert("Please select at least one organism");
		return (false);
		}	
	}
	else{
		 organism="all";
	}
	var validinput=keyword.replace(/[^a-zA-Z]+/g,'');	
	searchform.keyword.value=validinput;
	if(validinput.length>=3){
	//	alert(organism);
	searchform.organism_id.value=organism;
	searchform.organism_name.value="";
	document.searchform.submit();
	}
	else{
		alert("Please input a valid peptide at least 3 letters");
		searchform.keyword.focus();
		return (false);	
	}
	}
}
// all the following functions are for the taxon input hints 	
function inputSuggest() {  
if (window.XMLHttpRequest) {  
			     xmlHttp = new XMLHttpRequest();   
			  } else {  
			     xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");  
			  } 
	   var txtValue = document.getElementById('organism_name').value;  
	
	   xmlHttp.onreadystatechange = _handle;  
	   url = "organismhint.jsp?startwith=" + txtValue;  
	   xmlHttp.open("get", url, false);  
	   xmlHttp.send(null);  
	}
	
	function _handle() {  
	   if(xmlHttp.readyState==4){  
	      if(xmlHttp.status==200){  
	          var s = document.getElementById('result_display')  
	          s.innerHTML = xmlHttp.responseText;   
	      }  
	   }  
	}  
	function shiftFocus(e){
		   var keynum;
		    keynum = window.event ? e.keyCode : e.which;  
		   if(keynum=='40'){
			   document.getElementById('organism_select').focus(); 
		   }
	}
	function leftFocus(e){
		   var keynum;
		    keynum = window.event ? e.keyCode : e.which;  
		    if(keynum=='37'){
		    	 document.getElementById('organism_name').focus(); 
		    }
	}
	
	function checkEnter(e){
		   var keynum;
		    keynum = window.event ? e.keyCode : e.which;  
		 if(keynum=='13'){
			   setSuggestValue(document.getElementById('organism_select').value);   
			   return false;
		   }
	}
	  
	function setSuggestValue(value) {  
	   document.getElementById('organism_name').value = value;   
	   document.getElementById('keyword').focus();
	} 
	
	
	function show_orgInput(){	
	document.getElementById('organism_name_div').style.display='inline';
	document.getElementById('result_display').style.display='inline';
	document.getElementById('result_newline').style.display='inline'; 
	document.getElementById("organism_name").style.display='inline';
	document.getElementById("organism_name").value='Type an organism name or a taxon ID here';
	}
//	taxon input hints end

//close the taxon input
	function close_orgInput(){
	if(document.getElementById("organism_select")!=null)
	document.getElementById("organism_select").style.display='none';	
	document.getElementById('organism_name_div').style.display='none';
	document.getElementById('result_display').style.display='none';
	document.getElementById('result_newline').style.display='none';
	document.getElementById("organism_name").style.display='none';
	document.getElementById("organism_name").value='';
	}
// When user change the focus from the taxon input to the peptide input
//verify the taxon input
	function verifyOrganismInput(){
	var obj = document.getElementsByName("input_option");
	for (var i=0; i<obj.length; i++){
	if (obj[i].checked){
	var	option=obj[i].value;
	break;
	}}
	if(option=="input"){
		if(searchform.organism_name.value!=""){	
		if(searchform.organism_name.value.match(/^[1-9]/)==null||document.getElementById('organism_select')!=null){
	var organisms=searchform.organism_name.value.match(/\[(.*?)\]/);
	if(organisms==null){
		if(document.getElementById('organism_select')!=null){
		 document.getElementById('organism_name').value = document.getElementById('organism_select').value;
		}
		else{
			alert("Please input a valid organism name");
			document.getElementById('organism_name_div').style.display='inline';
			document.getElementById('organism_name').style.display='inline';
			document.getElementById('organism_name').focus();
			return (false);
		 }
	}
		}
	}
	else{
		alert("Please input a valid organism name");
		document.getElementById('organism_name_div').style.display='inline';
		document.getElementById('organism_name').style.display='inline';
		document.getElementById('organism_name').focus();
		return (false);
	}	
	}
	document.getElementById('result_display').innerHTML = ''; 	
	}
//show the taxon multiple selection	
	function showOrganism(str)
	{	
	var objs=document.getElementsByName("abanner");
	for(var i=0;i<objs.length;i++){
		if(objs[i].id==str)
			document.getElementById(objs[i].id).style.font="normal bold 13px Verdana, Tahoma, Arial, Helvetica, sans-serif";
		else
			document.getElementById(objs[i].id).style.font="normal normal 13px Verdana, Tahoma, Arial, Helvetica, sans-serif";
	}
		
	var xmlhttp;
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari
	  xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function()
	  {
	if(xmlhttp.readyState<4){
		document.getElementById("organism").innerHTML="Loading...";	
	}	
	
	  if (xmlhttp.readyState==4 && xmlhttp.status==200)
	    {
		// alert(xmlhttp.responseText);
	    document.getElementById("organism").innerHTML=xmlhttp.responseText;
	    show_organism_checked();
	    
	    }
	  }
	xmlhttp.open("GET","./showorganism.jsp?startwith="+str,true);
	xmlhttp.send();
	}
//change the size and display of the taxon multiple selection	 	
	function show_orgSelect(){
	document.getElementById("inputtd").style.width='1024';
	document.getElementById("th_formtitle").style.width='98%'
	document.getElementById("th_link").style.width='2%'
	document.getElementById("organismlink").style.display='inline';
	document.getElementById("organism").style.display='inline';	
	document.getElementById("show_selected_count").style.display='inline';	
	showOrganism("A");
	}
// close the taxon multiple selection	
	function close_orgSelect(){
	document.getElementById("inputtd").style.width='850';
	document.getElementById("th_formtitle").style.width='97%'
	document.getElementById("th_link").style.width='3%'
	document.getElementById("organismlink").style.display='none';
	document.getElementById("organism").style.display='none';
	organismlist.length = 0;
	document.getElementById("show_selected_count").innerHTML='';
	document.getElementById("show_selected_count").style.display='none';	
	}
//change the focus of the input_option to the default	
	function click_close(){
		close_orgSelect();
		var x=document.getElementsByName("input_option"); 
		  for(var i=0;i<x.length;i++){  
		        if(x[i].value=='all')   {  
		            x[i].checked=true;  
		            break;  
		        }  
		    }  
	}
