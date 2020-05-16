
                                                var yasgui = YASGUI(document.getElementById("yasgui"), {
                                                //Uncomment below to change the default endpoint
                                                //Note: If you've already opened the YASGUI page before, you should first clear your
                                                //local-storage cache before you will see the changes taking effect
                                                yasqe:{sparql:{endpoint:'https://sparql.proconsortium.org/virtuoso/sparql'}}
                                                });
                                                var yasqe = yasgui.current().yasqe;

                                                function loadQuery (queryname) {
                                                        //alert(yasqe.getValue());
                                                        //e.preventDefault();
                                                        jQuery.ajax({
                                                                url: "yasgui/queries/" + queryname + ".rq",
                                                                dataType: 'text',
                                                                success: function (data) {
									//alert(data);
                                                                        yasqe.setValue(data);
                                                                        yasqe.query();
                                                                }
                                                        });
                                                }

