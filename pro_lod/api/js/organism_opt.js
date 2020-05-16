
      function add_orgs(number,t) {
        var obj=document.getElementById('org_options')
		    var num=number
			var type=t
			var box_body=''

if (num==100) {
			var box_body='<img src=\"/pirwww/images/transparent_dot.png\" height=3 width=1><br><b>1. </b><a href=\"/pirwww/support/help.shtml#\" target=_blank>Select a taxon group</a>:'
}else {
			var box_body='<img src=\"/pirwww/images/transparent_dot.png\" height=3 width=1><br><b>1. </b><a href=\"/pirwww/support/help.shtml#\" target=_blank>Select an organism</a>:<br><img src=\"/pirwww/images/transparent_dot.png\" height=10>'
}


if (num==100) {

		box_body+='<INPUT type=hidden name=org_grp value=1>'

				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom TD colspan=13 nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=450 height=14><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD></TR>'


        box_body+='<TR><TD colspan=13 valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=300 height=20><img src=\"/pirwww/images/org_grp_id.png\"><img src=\"/pirwww/images/transparent_dot.png\" width=75 height=14></TD></TR>'


        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260 nowrap valign=top>'

box_body+='<input TYPE=RADIO NAME=dataset_name value=2157><a target=2157 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2157>Arch</a></a> [2157]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=28889><a target=62977 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28889>Arch/Crenar</a></a> [28889]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=28890><a target=28890 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28890>Arch/Euryar</a></a> [28890]<br>'

box_body+='<input TYPE=RADIO NAME=dataset_name value=2><a target=2 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2>Bac</a></a> [2]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=201174><a target=201174 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=201174>Bac/ActnBac</a></a> [201174]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=28211><a target=28211 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28211>Bac/Alpha-proteo</a></a> [28211]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=200783><a target=200783 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=200783>Bac/Aquific</a></a> [200783]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=28216><a target=28216 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28216>Bac/Beta-proteo</a></a> [28216]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=976><a target=976 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=976>Bac/CFB_bac</a></a> [976]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=204428><a target=204428 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=204428>Bac/Chlamyd</a></a> [204428]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=1117><a target=1117 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1117>Bac/CyanoBac</a></a> [1117]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=1297><a target=1297 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1297>Bac/Dein-Therm</a></a> [1297]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=68525><a target=68525 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=68525>Bac/Delta-Epsilon-proteo</a></a> [68525]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=1239><a target=1239 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1239>Bac/Firmicute</a></a> [1239]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=32066><a target=32066 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=32066>Bac/FusoBac</a></a> [32066]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=1236><a target=1236 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1236>Bac/Gamma-proteo</a></a> [1236]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=1090><a target=1090 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1090>Bac/Grn_sulf_Bac</a></a> [1090]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=203682><a target=203682 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=203682>Bac/Plnctmy</a></a> [203682]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=1224><a target=1224 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1224>Bac/Proteo</a></a> [1224]<br>'

        box_body+='</td><td nowrap valign=top>'


box_body+='<input TYPE=RADIO NAME=dataset_name value=200918><a target=200918 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=200918>Bac/Thrmtg</a></a> [200918]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=2759><a target=2759 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2759>Euk</a></a> [2759]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=33630><a target=33630 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33630>Euk/Alveolat</a></a> [33630]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=8292><a target=8292 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=8292>Euk/amphibian</a></a> [8292]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=33208><a target=33208 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33208>Euk/Animal</a></a> [33208]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=8782><a target=8782 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=8782>Euk/bird</a></a> [8782]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=3027><a target=3027 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=3027>Euk/Cryptpht</a></a> [3027]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=207245><a target=207245 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=207245>Euk/Dplmnad</a></a> [207245]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=33682><a target=33682 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33682>Euk/Euglenozoa</a></a> [33682]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=4751><a target=4751 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4751>Euk/Fungi</a></a> [4751]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=33154><a target=33154 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33154>Euk/Fungi-Metazoa</a></a> [33154]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=3041><a target=3041 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=3041>Euk/Grn_algae</a></a> [3041]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=40674><a target=40674 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=40674>Euk/mammal</a></a> [40674]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=142796><a target=142796 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=142796>Euk/Myctzoa</a></a> [142796]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=33090><a target=33090 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33090>Euk/Plant</a></a> [33090]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=2763><a target=2763 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2763>Euk/Red_algae</a></a> [2763]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=7742><a target=7742 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=7742>Euk/Vertebrata</a></a> [7742]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=10239><a target=10239 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=10239>Virus</a></a> [10239]<br>'
box_body+='<input TYPE=RADIO NAME=dataset_name value=35268><a target=35268 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=35268>Vir/Retro-transc</a></a> [35268]<br>'


        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'

} else if (num==1) {

				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0><br><br></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'


        box_body+='<TR><TD colspan=13 valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20><img src=\"/pirwww/images/org_nm_id.png\"><img src=\"/pirwww/images/transparent_dot.png\" width=75 height=14></TD></TR>'


        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260 nowrap valign=top>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=62977><a target=62977 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=62977>Acinetobacter sp.</a></a> [62977]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=56636><a target=56636 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=56636>Aeropyrum pernix</a> [56636]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=176299><a target=176299 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=176299>Agrobacterium tumefaciens ..</a> [176299]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=103690><a target=103690 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=103690>Anabaena sp.</a> [103690]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1172><a target=1172 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1172>Anabaena variabilis</a> [1172]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=234826><a target=234826 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=234826>Anaplasma marginale</a> [234826]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=7165><a target=7165 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=7165>Anopheles gambiae</a> [7165]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=63363><a target=63363 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=63363>Aquifex aeolicus</a> [63363]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=3702><a target=3702 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=3702>Arabidopsis thaliana</a> [3702]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2234><a target=2234 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2234>Archaeoglobus fulgidus</a> [2234]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=33169><a target=33169 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33169>Ashbya gossypii</a> [33169]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=5085><a target=5085 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=5085>Aspergillus fumigatus</a> [5085]<br>'

		box_body+='<input TYPE=RADIO NAME=dataset_name value=4498><a target=4498 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4498>Avena sativa</a></a> [4498]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=76114><a target=76114 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=76114>Azoarcus sp.</a> [76114]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1392><a target=1392 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1392>Bacillus anthracis</a> [1392]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=222523><a target=222523 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=222523>Bacillus cereus ATCC 10987</a> [222523]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=226900><a target=226900 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=226900>Bacillus cereus ATCC 14579</a> [226900]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=288681><a target=288681 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=288681>Bacillus cereus E33L</a> [288681]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=66692><a target=66692 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=66692>Bacillus clausii</a> [66692]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=86665><a target=86665 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=86665>Bacillus halodurans</a> [86665]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=279010><a target=279010 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=279010>Bacillus licheniformis</a> [279010]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1423><a target=1423 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1423>Bacillus subtilis</a> [1423]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=180856><a target=180856 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=180856>Bacillus thuringiensis subsp.</a> [180856]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=817><a target=817 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=817>Bacteroides fragilis</a> [817]<br>'


        box_body+='</td><td nowrap valign=top>'


        box_body+='<input TYPE=RADIO NAME=dataset_name value=272559><a target=272559 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=272559>Bacteroides fragilis</a> [272559]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=818><a target=818 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=818>Bacteroides thetaiotaomicron</a> [818]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=38323><a target=38323 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=38323>Bartonella henselae</a> [38323]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=803><a target=803 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=803>Bartonella quintana</a> [803]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=959><a target=959 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=959>Bdellovibrio bacteriovorus</a> [959]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=216816><a target=216816 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=216816>Bifidobacterium longum</a> [216816]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=203907><a target=203907 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=203907>Blochmannia floridanus</a> [203907]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=291272><a target=291272 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=291272>Blochmannia pennsylvanicus</a> [291272]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=518><a target=518 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=518>Bordetella bronchiseptica</a> [518]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=519><a target=519 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=519>Bordetella parapertussis</a> [519]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=520><a target=520 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=520>Bordetella pertussis</a> [520]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=139><a target=139 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=139>Borrelia burgdorferi</a> [139]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=29519><a target=29519 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=29519>Borrelia garinii</a> [29519]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=7955><a target=7955 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=7955>Brachydanio rerio</a> [7955]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=375><a target=375 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=375>Bradyrhizobium japonicum</a> [375]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=235><a target=235 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=235>Brucella abortus</a> [235]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=29459><a target=29459 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=29459>Brucella melitensis</a> [29459]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=29461><a target=29461 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=29461>Brucella suis</a> [29461]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=118099><a target=118099 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=118099>Buchnera aphidicola (A. pisum)</a> [118099]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=135842><a target=135842 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=135842>Buchnera aphidicola (B. p.)</a> [135842]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=98794><a target=98794 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=98794>Buchnera aphidicola (S. g.)</a> [98794]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=13373><a target=13373 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=13373>Burkholderia mallei</a> [13373]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=28450><a target=28450 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28450>Burkholderia pseudomallei</a> [28450]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=269483><a target=269483 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=269483>Burkholderia sp. 383</a> [269483]<br>'




        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'

} else if (num==2) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'

        box_body+='			<td><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0><br><br></TD>'

        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'



        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'


        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260 valign=top>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=6238><a target=6238 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=6238>Caenorhabditis briggsae</a> [6238]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=6239><a target=6239 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=6239>Caenorhabditis elegans</a> [6239]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=197><a target=197 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=197>Campylobacter jejuni</a> [197]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=195099><a target=195099 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=195099>Campylobacter jejuni RM1221</a> [195099]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=5478><a target=5478 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=5478>Candida glabrata</a> [5478]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=264201><a target=264201 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=264201>Candidatus Protochlamydia ..</a> [264201]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=246194><a target=246194 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=246194>Carboxydothermus hydr. ..</a> [246194]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=155892><a target=155892 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=155892>Caulobacter crescentus</a> [155892]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=83560><a target=83560 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=83560>Chlamydia muridarum</a> [83560]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=83558><a target=83558 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=83558>Chlamydia pneumoniae</a> [83558]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=813><a target=813 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=813>Chlamydia trachomatis</a> [813]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=83555><a target=83555 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=83555>Chlamydophila abortus</a> [83555]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=83557><a target=83557 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=83557>Chlamydophila caviae</a> [83557]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=340177><a target=340177 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=340177>Chlorobium chloro. ..</a> [340177]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1097><a target=1097 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1097>Chlorobium tepidum</a> [1097]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=536><a target=536 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=536>Chromobacterium violaceum</a> [536]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1488><a target=1488 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1488>Clostridium acetobutylicum</a> [1488]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1502><a target=1502 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1502>Clostridium perfringens</a> [1502]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1513><a target=1513 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1513>Clostridium tetani</a> [1513]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=167879><a target=167879 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=167879>Colwellia psych.</a> [167879]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1717><a target=1717 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1717>Corynebacterium diphtheriae</a> [1717]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=152794><a target=152794 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=152794>Corynebacterium efficiens</a> [152794]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=152794><a target=152794 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=152794>Corynebacterium glutamicum</a> [152794]<br>'




        box_body+='</td><td nowrap valign=top>'


        box_body+='<input TYPE=RADIO NAME=dataset_name value=306537><a target=306537 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=306537>Corynebacterium jeikeium</a> [306537]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=777><a target=777 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=777>Coxiella burnetii</a> [777]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=5207><a target=5207 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=5207>Cryptococcus neoformans</a> [5207]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=4959><a target=4959 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4959>Debaryomyces hansenii</a> [4959]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=159087><a target=159087 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=159087>Dechloromonas aromatica</a> [159087]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=243164><a target=243164 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=243164>Dehalococcoides ethen.</a> [243164]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=255470><a target=255470 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=255470>Dehalococcoides sp.</a> [255470]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1299><a target=1299 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1299>Deinococcus radiodurans</a> [1299]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=84980><a target=84980 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=84980>Desulfotalea psychrophila</a> [84980]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=207559><a target=207559 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=207559>Desulfovibrio desul. ..</a> [207559]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=882><a target=882 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=882>Desulfovibrio vulgaris ..</a> [882]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=44689><a target=44689 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=44689>Dictyostelium discoideum</a> [44689]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=7227><a target=7227 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=7227>Drosophila melanogaster</a> [7227]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=269484><a target=269484 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=269484>Ehrlichia canis</a> [269484]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=302409><a target=302409 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=302409>Ehrlichia ruminantium str. G.</a> [302409]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=254945><a target=254945 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=254945>Ehrlichia ruminantium str. W.</a> [254945]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=6035><a target=6035 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=6035>Encephalitozoon cuniculi</a> [6035]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1351><a target=1351 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1351>Enterococcus faecalis</a> [1351]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=314225><a target=314225 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=314225>Erythrobacter litoralis</a> [314225]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=562><a target=562 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=562>Escherichia coli</a> [562]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=83334><a target=83334 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=83334>Escherichia coli O157:H7</a> [83334]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=217992><a target=217992 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=217992>Escherichia coli O6</a> [217992]<br>'

        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'

} else if (num==3) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'

        box_body+='			<td><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0><br><br></TD>'

		box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'


        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'


        box_body+='<TR><TD colspan=13>'

        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260  valign=top>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=119856><a target=119856 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=119856>Francisella tularensis ..</a> [119856]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=76856><a target=76856 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=76856>Fusobacterium nucleatum ..</a> [76856]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=9031><a target=9031 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=9031>Gallus gallus</a> [9031]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1462><a target=1462 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1462>Geobacillus kaustophilus</a> [1462]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=269799><a target=269799 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=269799>Geobacter metallireducens</a> [269799]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=35554><a target=35554 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=35554>Geobacter sulfurreducens</a> [35554]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=5518><a target=5518 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=5518>Gibberella zeae</a> [5518]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=33072><a target=33072 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33072>Gloeobacter violaceus</a> [33072]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=442><a target=442 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=442>Gluconobacter oxydans</a> [442]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=55529><a target=55529 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=55529>Guillardia theta</a> [55529]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=730><a target=730 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=730>Haemophilus ducreyi</a> [730]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=727><a target=727 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=727>Haemophilus i. 86-028NP</a> [727]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=281310><a target=281310 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=281310>Haemophilus influenzae</a> [281310]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2238><a target=2238 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2238>Haloarcula marismortui</a> [2238]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2242><a target=2242 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2242>Halobacterium salinarium</a> [2242]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=32025><a target=32025 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=32025>Helicobacter hepaticus</a> [32025]<br>'			
        box_body+='<input TYPE=RADIO NAME=dataset_name value=210><a target=210 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=210>Helicobacter pylori</a> [210]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=85963><a target=85963 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=85963>Helicobacter pylori J99</a> [85963]<br>'	

				box_body+='</td><td nowrap valign=top>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=9606><a target=9606 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=9606>Homo sapiens</a> [9606]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=4513><a target=4513 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4513>Hordeum vulgare</a> [4513]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=135577><a target=135577 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=135577>Idiomarina loihiensis</a> [135577]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=28985><a target=28985 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28985>Kluyveromyces lactis</a> [28985]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1579><a target=1579 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1579>Lactobacillus acidophilus</a> [1579]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=33959><a target=33959 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33959>Lactobacillus johnsonii</a> [33959]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1590><a target=1590 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1590>Lactobacillus plantarum</a> [1590]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=314315><a target=314315 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=314315>Lactobacillus sakei ..</a> [314315]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1360><a target=1360 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1360>Lactococcus lactis ..</a> [1360]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=297245><a target=297245 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=297245>Legionella p. str. Lens</a> [297245]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=297246><a target=297246 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=297246>Legionella p. str. Paris</a> [297246]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=272624><a target=272624 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=272624>Legionella pneumophila ..</a> [272624]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=59736><a target=59736 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=59736>Leifsonia xyli ..</a> [59736]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=5664><a target=5664 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=5664>Leishmania major</a> [5664]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=173><a target=173 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=173>Leptospira interrogans</a> [173]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=44275><a target=44275 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=44275>Leptospira interrogans ..</a> [44275]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1642><a target=1642 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1642>Listeria innocua</a> [1642]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1639><a target=1639 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1639>Listeria monocytogenes</a> [1639]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=265669><a target=265669 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=265669>Listeria m. str. 4b F2365</a> [265669]<br>'


        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'
} else if (num==4) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'

		box_body+='			<td><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0><br><br></TD>'

        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'


        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'



        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260>'


			
        box_body+='<input TYPE=RADIO NAME=dataset_name value=342108><a target=342108 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=342108>Magnetospirillum magnet. ..</a> [342108]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=221988><a target=221988 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=221988>Mannheimia succinici. ..</a> [221988]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2151><a target=2151 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2151>Mesoplasma florum</a> [2151]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=187420><a target=187420 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=187420>Methanobacterium thermo..</a> [187420]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2190><a target=2190 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2190>Methanococcus jannaschii</a> [2190]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=39152><a target=39152 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=39152>Methanococcus maripaludis</a> [39152]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2320><a target=2320 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2320>Methanopyrus kandleri</a> [2320]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2214><a target=2214 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2214>Methanosarcina acetivorans</a> [2214]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2208><a target=2208 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2208>Methanosarcina barkeri</a> [2208]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=269797><a target=269797 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=269797>Methanosarcina b. str. fusaro</a> [269797]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2209><a target=2209 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2209>Methanosarcina mazei</a> [2209]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=414><a target=414 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=414>Methylococcus capsulatus</a> [414]<br>'				
				
        box_body+='<input TYPE=RADIO NAME=dataset_name value=10090><a target=10090 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=10090>Mus musculus</a> [10090]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1765><a target=1765 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1765>Mycobacterium bovis</a> [1765]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1769><a target=1769 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1769>Mycobacterium leprae</a> [1769]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1770><a target=1770 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1770>Mycobacterium paratuberculosis</a> [1770]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1773><a target=1773 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1773>Mycobacterium tuberculosis</a> [1773]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2096><a target=2096 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2096>Mycoplasma gallisepticum</a> [2096]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2097><a target=2097 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2097>Mycoplasma genitalium</a> [2097]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=295358><a target=295358 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=295358>Mycoplasma h. 232</a> [295358]<br>'


				box_body+='</td><td nowrap>'


        box_body+='<input TYPE=RADIO NAME=dataset_name value=262722><a target=262722 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=262722>Mycoplasma h. 7448</a> [262722]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=262719><a target=262719 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=262719>Mycoplasma h. J</a> [262719]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2118><a target=2118 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2118>Mycoplasma mobile</a> [2118]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=44101><a target=44101 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=44101>Mycoplasma mycoides ..</a> [44101]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=28227><a target=28227 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=28227>Mycoplasma penetrans</a> [28227]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2104><a target=2104 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2104>Mycoplasma pneumoniae</a> [2104]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2107><a target=2107 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2107>Mycoplasma pulmonis</a> [2107]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=262723><a target=262723 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=262723>Mycoplasma synoviae</a> [262723]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=160232><a target=160232 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=160232>Nanoarchaeum equitans</a> [160232]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=348780><a target=348780 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=348780>Natronomonas pharaonis ..</a> [348780]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=242231><a target=242231 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=242231>Neisseria gonorrhoeae ..</a> [242231]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=65699><a target=65699 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=65699>Neisseria meningitidis ..</a> [65699]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=491><a target=491 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=491>Neisseria meningitidis ..</a> [491]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=323098><a target=323098 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=323098>Nitrobacter winogradskyi ..</a> [323098]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=323261><a target=323261 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=323261>Nitrosococcus oceani ..</a> [323261]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=915><a target=915 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=915>Nitrosomonas europaea</a> [915]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=323848><a target=323848 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=323848>Nitrosospira multiformis ..</a> [323848]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=37329><a target=37329 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=37329>Nocardia farcinica</a> [37329]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=182710><a target=182710 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=182710>Oceanobacillus iheyensis</a> [182710]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=100379><a target=100379 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=100379>Onion yellows phytoplasma</a> [100379]<br>'




        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'
} else if (num==5) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'

        box_body+='			<td><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0><br><br></TD>'

		box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'



        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'




        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260>'



        box_body+='<input TYPE=RADIO NAME=dataset_name value=5888><a target=5888 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=5888>Paramecium tetraurelia</a> [5888]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=747><a target=747 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=747>Pasteurella multocida</a> [747]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=29471><a target=29471 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=29471>Pectobacterium atrosepticum</a> [29471]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=335992><a target=335992 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=335992>Pelagibacter ubique</a> [335992]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=338963><a target=338963 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=338963>Pelobacter carbinolicus ..</a> [338963]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=319225><a target=319225 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=319225>Pelodictyon luteolum ..</a> [319225]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=74109><a target=74109 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=74109>Photobacterium profundum</a> [74109]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=141679><a target=141679 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=141679>Photorhabdus luminescens ..</a> [141679]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=82076><a target=82076 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=82076>Picrophilus torridus</a> [82076]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=36329><a target=36329 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=36329>Plasmodium falciparum</a> [36329]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=73239><a target=73239 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=73239>Plasmodium yoelii yoelii</a> [73239]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=837><a target=837 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=837>Porphyromonas gingivalis</a> [837]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1219><a target=1219 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1219>Prochlorococcus marinus</a> [1219]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=74547><a target=74547 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=74547>Prochlorococcus marinus ..</a> [74547]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=59920><a target=59920 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=59920>Prochlorococcus marinus</a> [59920]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=59919><a target=59919 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=59919>Prochlorococcus marinus ..</a> [59919]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1747><a target=1747 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1747>Propionibacterium acnes</a> [1747]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=326442><a target=326442 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=326442>Pseudoalteromonas halop. ..</a> [326442]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=287><a target=287 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=287>Pseudomonas aeruginosa</a> [287]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=220664><a target=220664 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=220664>Pseudomonas fluorescens Pf-5</a> [220664]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=160488><a target=160488 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=160488>Pseudomonas putida</a> [160488]<br>'
				
				
				box_body+='</td><td nowrap>'


        box_body+='<input TYPE=RADIO NAME=dataset_name value=264730><a target=264730 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=264730>Pseudomonas s. pv. p. 1448A</a> [264730]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=205918><a target=205918 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=205918>Pseudomonas s. pv. s. B728a</a> [205918]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=323><a target=323 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=323>Pseudomonas s. pv. s. B728a</a> [323]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=334543><a target=334543 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=334543>Psychrobacter arcticum</a> [334543]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=13773><a target=13773 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=13773>Pyrobaculum aerophilum</a> [13773]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=29292><a target=29292 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=29292>Pyrococcus abyssi</a> [29292]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2261><a target=2261 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2261>Pyrococcus furiosus</a> [2261]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=53953><a target=53953 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=53953>Pyrococcus horikoshii</a> [53953]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=69014><a target=69014 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=69014>Pyrococcus kodakaraensis</a> [69014]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=264198><a target=264198 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=264198>Ralstonia eutropha JMP134</a> [264198]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=305><a target=305 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=305>Ralstonia solanacearum</a> [305]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=10116><a target=10116 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=10116>Rattus norvegicus</a> [10116]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=381><a target=381 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=381>Rhizobium loti</a> [381]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=382><a target=382 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=382>Rhizobium meliloti</a> [382]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=272943><a target=272943 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=272943>Rhodobacter sphaeroides 2.4.1</a> [272943]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=117><a target=117 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=117>Rhodopirellula baltica</a> [117]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1076><a target=1076 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1076>Rhodopseudomonas palustris</a> [1076]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=781><a target=781 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=781>Rickettsia conorii</a> [781]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=42862><a target=42862 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=42862>Rickettsia felis</a> [42862]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=782><a target=782 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=782>Rickettsia prowazekii</a> [782]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=785><a target=785 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=785>Rickettsia typhi</a> [785]<br>'



        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'
} else if (num==6) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'

		box_body+='			<td><img src=/pirwww/images/s_s.png border=0><br><br></TD>'

        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'


        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'



        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260 nowrap valign=top>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=4932><a target=4932 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4932>Saccharomyces cerevisiae</a> [4932]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=591><a target=591 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=591>Salmonella choleraesuis</a> [591]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=54388><a target=54388 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=54388>Salmonella paratyphi-a</a> [54388]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=601><a target=601 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=601>Salmonella typhi</a> [601]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=602><a target=602 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=602>Salmonella typhimurium</a> [602]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=4896><a target=4896 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4896>Schizosaccharomyces pombe</a> [4896]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=4550><a target=4550 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4550>Secale cereale</a> [4550]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=70863><a target=70863 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=70863>Shewanella oneidensis</a> [70863]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=300268><a target=300268 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=300268>Shigella boydii ..</a> [300268]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=300267><a target=300267 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=300267>Shigella dysenteriae ..</a> [300267]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=623><a target=623 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=623>Shigella flexneri</a> [623]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=300269><a target=300269 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=300269>Shigella sonnei</a> [300269]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=89184><a target=89184 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=89184>Silicibacter pomeroyi</a> [89184]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=93062><a target=93062 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=93062>S. a. subsp. a. COL</a> [93062]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=282458><a target=282458 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=282458>S. a. subsp. a. MRSA252</a> [282458]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=282459><a target=282459 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=282459>S. a. subsp. a. MSSA476</a> [282459]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=158878><a target=158878 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=158878>S. a. subsp. a. Mu50</a> [158878]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=196620><a target=196620 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=196620>S. a. subsp. a. MW2</a> [196620]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=158879><a target=158879 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=158879>S. a. subsp. a. N315</a> [158879]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=176280><a target=176280 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=176280>Staphylococcus epidermidis</a> [176280]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=176279><a target=176279 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=176279>Staphylococcus epider. ..</a> [176279]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=279808><a target=279808 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=279808>Staphylococcus haemo. ..</a> [279808]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=342451><a target=342451 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=342451>Staphylococcus sapro. ..</a> [342451]<br>'
		
			
				box_body+='</td><td nowrap valign=top>'


        box_body+='<input TYPE=RADIO NAME=dataset_name value=355315><a target=355315 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=355315>Streptococcus a. serogroup Ia</a> [355315]<br>'				
        box_body+='<input TYPE=RADIO NAME=dataset_name value=216495><a target=216495 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=216495>Streptococcus a. serogroup III</a> [216495]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=216466><a target=216466 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=216466>Streptococcus a. serogroup V</a> [216466]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1309><a target=1309 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1309>Streptococcus mutans</a> [1309]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1313><a target=1313 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1313>Streptococcus pneumoniae</a> [1313]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=171101><a target=171101 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=171101>Streptococcus pneu. ..</a> [171101]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=301447><a target=301447 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=301447>Streptococcus p. serotype M1</a> [301447]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=301451><a target=301451 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=301451>Streptococcus p. serotype M18</a> [301451]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=319700><a target=319700 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=319700>Streptococcus p. serotype M28</a> [319700]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=301448><a target=301448 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=301448>Streptococcus p. serotype M3</a> [301448]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=301450><a target=301450 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=301450>Streptococcus p. serotype M6</a> [301450]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=264199><a target=264199 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=264199>Streptococcus t. LMG 18311</a> [264199]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=299768><a target=299768 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=299768>Streptococcus t. CNRZ1066</a> [299768]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=33903><a target=33903 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=33903>Streptomyces avermitilis</a> [33903]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1902><a target=1902 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1902>Streptomyces coelicolor</a> [1902]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2285><a target=2285 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2285>Sulfolobus acidocaldarius</a> [2285]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2287><a target=2287 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2287>Sulfolobus solfataricus</a> [2287]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=111955><a target=111955 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=111955>Sulfolobus tokodaii</a> [111955]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2734><a target=2734 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2734>Symbiobacterium thermophilum</a> [2734]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=32046><a target=32046 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=32046>Synechococcus elongatus</a> [32046]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=269084><a target=269084 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=269084>Synechococcus e. PCC 6301</a> [269084]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=84588><a target=84588 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=84588>Synechococcus sp. WH 8102</a> [84588]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=1148><a target=1148 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1148>Synechocystis sp.</a> [1148]<br>'



        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'
} else if (num==7) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'

        box_body+='			<td><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0><br><br></TD>'

        box_body+='			<td><a href="#" onclick="add_orgs(8,'+type+');return false;"><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'


        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'



        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260 nowrap valign=top>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=99883><a target=99883 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=99883>Tetraodon nigroviridis</a> [99883]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=119072><a target=119072 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=119072>Thermoanaerobacter teng.</a> [119072]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=269800><a target=269800 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=269800>Thermobifida fusca</a> [269800]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2303><a target=2303 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2303>Thermoplasma acidophilum</a> [2303]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=50339><a target=50339 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=50339>Thermoplasma volcanium</a> [50339]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2336><a target=2336 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2336>Thermotoga maritima</a> [2336]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=262724><a target=262724 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=262724>Thermus thermophilus HB27</a> [262724]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=300852><a target=300852 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=300852>Thermus thermophilus HB8</a> [300852]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=292415><a target=292415 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=292415>Thiobacillus denitrificans ..</a> [292415]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=317025><a target=317025 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=317025>Thiomicrospira crunogena</a> [317025]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=326298><a target=326298 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=326298>Thiomicrospira denitrificans ..</a> [326298]<br>'
 

				box_body+='</td><td nowrap valign=top>'


	    box_body+='<input TYPE=RADIO NAME=dataset_name value=158><a target=158 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=158>Treponema denticola</a> [158]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=160><a target=160 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=160>Treponema pallidum</a> [160]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=4565><a target=4565 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4565>Triticum aestivum</a> [4565]<br>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=218496><a target=218496 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=218496>Tropheryma whipplei TW08/27</a> [218496]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=203267><a target=203267 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=203267>Tropheryma w. str. Twist</a> [203267]<br>'	
        box_body+='<input TYPE=RADIO NAME=dataset_name value=134821><a target=134821 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=134821>Ureaplasma parvum</a> [134821]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=666><a target=666 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=666>Vibrio cholerae</a> [666]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=312309><a target=312309 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=312309>Vibrio fischeri ES114</a> [312309]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=670><a target=670 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=670>Vibrio parahaemolyticus</a> [670]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=672><a target=672 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=672>Vibrio vulnificus</a> [672]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=196600><a target=196600 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=196600>Vibrio vulnificus YJ016</a> [196600]<br>'



        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'
} else if (num==8) {
				box_body+='<TABLE border=0 cellspacing=2 cellpadding=0 class=nrm11>'

        box_body+='<TR><TD valign=bottom nowrap><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=14></TD>'
        box_body+='			<td><img src=\"/pirwww/images/point_right.png\"></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(1,'+type+');return false;"><img src=/pirwww/images/s_a.png border=0><img src=/pirwww/images/s_b.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(2,'+type+');return false;"><img src=/pirwww/images/s_c.png border=0><img src=/pirwww/images/s_d.png border=0><img src=/pirwww/images/s_e.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(3,'+type+');return false;"><img src=/pirwww/images/s_f.png border=0><img src=/pirwww/images/s_g.png border=0><img src=/pirwww/images/s_h.png border=0><img src=/pirwww/images/s_i.png border=0><img src=/pirwww/images/s_j.png border=0><img src=/pirwww/images/s_k.png border=0><img src=/pirwww/images/s_l.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(4,'+type+');return false;"><img src=/pirwww/images/s_m.png border=0><img src=/pirwww/images/s_n.png border=0><img src=/pirwww/images/s_o.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(5,'+type+');return false;"><img src=/pirwww/images/s_p.png border=0><img src=/pirwww/images/s_q.png border=0><img src=/pirwww/images/s_r.png border=0></a></TD>'
		box_body+='			<td><a href="#" onclick="add_orgs(6,'+type+');return false;"><img src=/pirwww/images/s_s.png border=0></a></TD>'
        box_body+='			<td><a href="#" onclick="add_orgs(7,'+type+');return false;"><img src=/pirwww/images/s_t.png border=0><img src=/pirwww/images/s_u.png border=0><img src=/pirwww/images/s_v.png border=0></a></TD>'

        box_body+='			<td><img src=/pirwww/images/s_w.png border=0><img src=/pirwww/images/s_x.png border=0><img src=/pirwww/images/s_y.png border=0><img src=/pirwww/images/s_z.png border=0><br><br></TD>'

		box_body+='			<td><a href="#" onclick="add_orgs(0,'+type+');return false;"><img src=/pirwww/images/off.png border=0></a></TD>'
        box_body+='			<td><img src=\"/pirwww/images/transparent_dot.png\" width=100 height=16></TD></TR>'


        box_body+='<TR><TD colspan=13><img src=\"/pirwww/images/transparent_dot.png\" width=60 height=20></TD></TR>'



        box_body+='<TR><TD colspan=13>'
        box_body+='<table border=0 cellspacing=0 cellpadding=0 class=nrm11><tr><td width=260 nowrap valign=top>'


        box_body+='<input TYPE=RADIO NAME=dataset_name value=36870><a target=36870 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=36870>Wigglesworthia glossinidia ..</a> [36870]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=66077><a target=66077 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=66077>Wolbachia pipientis wMel</a> [66077]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=292805><a target=292805 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=292805>Wolbachia sp. ..</a> [292805]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=844><a target=844 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=844>Wolinella succinogenes</a> [62977]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=92829><a target=92829 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=92829>Xanthomonas axonopodis ..</a> [92829]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=340><a target=340 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=340>Xanthomonas c. pv. c.</a> [340]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=314565><a target=314565 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=314565>X. c. pv. c. str. 8004</a> [314565]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=316273><a target=316273 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=316273>X. c. pv. v. str. 85-10</a> [316273]<br>'


        box_body+='</td><td valign=top nowrap>'

        box_body+='<input TYPE=RADIO NAME=dataset_name value=64187><a target=64187 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=64187>Xanthomonas oryzae ..</a> [64187]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=2371><a target=2371 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=2371>Xylella fastidiosa</a> [2371]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=183190><a target=183190 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=183190>Xylella fastidiosa Temecula1</a> [183190]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=4952><a target=4952 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=4952>Yarrowia lipolytica</a> [4952]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=632><a target=632 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=632>Yersinia pestis</a> [632]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=633><a target=633 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=633>Yersinia pseudotuberculosis</a> [633]<br>'
        box_body+='<input TYPE=RADIO NAME=dataset_name value=542><a target=542 href=http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=542>Zymomonas mobilis</a> [542]<br>'
				

        box_body+='</td></tr></table>'
        box_body+='</TD></TR></table>'
}


		    document.getElementById('org_options').innerHTML=box_body


if (num==0) {
        var obj=document.getElementById('org_options')

				var box_body='<b>1. </b><a href=\"/pirwww/support/help.shtml#3\" target=_blank>Select a database</a>:<img src=\"/pirwww/images/transparent_dot.png\" height=4 width=30><input TYPE=RADIO NAME=dataset_name checked><b><a  href=\"http://pir.uniprot.org/database/DBDescription.shtml#uniprot\">UniProtKB</a></b><img src=\"/pirwww/images/transparent_dot.png\" height=4 width=10>(or restricted by <a href="#" onclick="add_orgs(1,'+type+');return false;">organism</a>/<a href="#" onclick="add_orgs(100,'+type+');return false;">taxon group</a>)<br><img src=\"/pirwww/images/transparent_dot.png\" height=4 width=175><input TYPE=RADIO NAME=dataset_name value=uniref><a href=\"http://pir.uniprot.org/database/DBDescription.shtml#uniref\"><b>UniRef100</b></a>'
				if (type==2) {
					box_body='<b>1. </b><a href=\"/pirwww/support/help.shtml#3\" target=_blank>Select a database</a>:<img src=\"/pirwww/images/transparent_dot.png\" height=4 width=30><input TYPE=RADIO NAME=dataset_name><b><a  href=\"http://pir.uniprot.org/database/DBDescription.shtml#uniprot\">UniProtKB</a></b><img src=\"/pirwww/images/transparent_dot.png\" height=4 width=10>(or restricted by <a href=# onclick=\"add_orgs(1,2);return false;\">organism</a>/<a href="#" onclick="add_org(100,2);return false;">taxon group</a>)<br><img src=\"/pirwww/images/transparent_dot.png\" height=4 width=175><input TYPE=RADIO NAME=dataset_name value=uniref><a href=\"http://pir.uniprot.org/database/DBDescription.shtml#uniref\"><b>UniRef100</b></a><br><img src=\"/pirwww/images/transparent_dot.png\" height=4 width=175><input TYPE=RADIO checked NAME=dataset_name value=cg><a href=\"http://pir.uniprot.org/database/DBDescription.shtml#cg\"><b>NIAID Biodefense Proteomics</b></a>'
				
				}
        document.getElementById('org_options').innerHTML=box_body


}


				return false
      }



