import modules as md
import Confluence_wiki


def generateReport():
    # A global variable to use across function.
    global cust_template
    cust_template = str()

    # Confluence template for web and api domain.
    web_api_template = '<h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:local-id="bfb9d815-bd1f-49af-bef0-55bd619c4dec" ac:macro-id="5658bb63-055e-4065-9630-2f2f67fcceab"><ac:parameter ac:name="">scroll-bookmark-1</ac:parameter></ac:structured-macro><span style="color: rgb(23,43,77);">This is the Validation TR for:</span></h1><ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" data-layout="default" ac:local-id="491dae03-06aa-490e-a6b1-deb95fbe4d8c" ac:macro-id="9e10dd27-5187-432d-935b-0b087f52a41c"><ac:plain-text-body><![CDATA[*TR_TITLE* \n*+Pre-requisites:+*]]></ac:plain-text-body></ac:structured-macro><ul><li><p>Access to xxxx Cloud WAF console (provided by GSOC team - POC Shruti SUMAN / Mohamed FANGAR): <br /><a href="https://my.xxxx.com/admin/login">https://my.xxxx.com/admin/login</a></p></li><li><p>Have installed dig command (on Windows: BIND <a href="https://www.isc.org/download/">download</a> link)</p></li></ul><table data-table-width="1800" data-layout="full-width" ac:local-id="99425094-5712-4066-b468-5855d4dc246f"><colgroup><col style="width: 359.0px;" /><col style="width: 359.0px;" /><col style="width: 359.0px;" /><col style="width: 386.0px;" /><col style="width: 332.0px;" /><col style="width: 332.0px;" /></colgroup><tbody><tr><td><p><strong>Steps</strong></p></td><td><p><strong>Expected result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </strong></p></td><td><p><strong>Help</strong></p></td><td><p><strong>Activity Status</strong></p></td><td><p><strong>Status</strong></p></td><td><p /></td></tr><tr><td><p><strong><u>Pre1</u></strong></p><p>xxxx Configuration Checking</p></td><td><p><u>On the xxxx admin portal / Edit Settings</u><br /><br /><u>xxxx web portal:</u></p><p>&nbsp; Is domain defined on the xxxx console?</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Yes, domain exists</p></td><td><p><br /></p></td><td><p><a href="http://WEB_DOMAIN">WEB_DOMAIN</a> </p><p><a href="http://API_DOMAIN">API_DOMAIN</a> </p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="720" ac:original-width="1280" ac:width="408"><ri:attachment ri:filename="domainWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><ac:image ac:align="center" ac:layout="center" ac:original-height="720" ac:original-width="1280" ac:custom-width="true" ac:width="370"><ri:attachment ri:filename="domainAPI_DOMAIN.png" ri:version-at-save="1" /></ac:image><p> </p></td><td><p>OK<br /><br /><br /></p></td><td><p /></td></tr><tr><td><p><br /></p></td><td><p>&nbsp; Do the Origin DNSs exist?</p><p><em>Make sure the Origin CNAME(s) domain is/are well setup: </em></p><p><br /><em>AERE (1 domain): Typically </em><br /><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </em><a href="http://origin-xxxxx.xxxx.com"><em>origin-xxxxx.xxxx.com</em></a> <br /><br /><em>DES (2 domains): Typically: </em><br /><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; origin-xx&lt;product&gt;-</em><a href="http://web.xxxx.com"><em>web.xxxx.com</em></a> &nbsp;&nbsp;&nbsp;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>digital touchpoints. &lt;airline name&gt;.</em><a href="http://airlines.api.xxxx.com"><em>airlines.api.xxxx.com</em></a></p></td><td><p>Website settings &gt; Origin servers<br /><br /><br />Website settings &gt; General</p></td><td><p>Ok origin exists for this airline domain.<br />AIRLINE_TYPE: </p><p>&lt;Origin_web_domain&gt;:  <a href="http://WEB_ORIGIN">WEB_ORIGIN</a>   </p><p>&lt;Origin_api_domain&gt;:  <a href="http://API_ORIGIN">API_ORIGIN</a>   </p><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="originWEB_DOMAIN.png" ac:width="370"><ri:attachment ri:filename="originWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="originAPI_DOMAIN.png" ac:width="370"><ri:attachment ri:filename="originAPI_DOMAIN.png" ri:version-at-save="1" /></ac:image></td><td><p><br /></p></td><td><p /></td></tr><tr><td><p><br /></p></td><td><p><strong><u>xxxx WAF portal:</u></strong> <br />All parameters are configured in BLOCKING mode</p></td><td><p>Website settings &gt;<br />WAF<br /><br /><br />SERVICES &gt; WAF &gt; WAF Policies</p></td><td><p><br /></p><p>DDOS for both web and api domains set to automatic.</p></td><td><p><br /></p></td><td><p /></td></tr><tr><td><p><br /></p></td><td><p>Review xxxx target DNS CNAME settings. <br /><br />Then, make sure they MATCH with the settings mentioned...<br />- ... in the Task Record <br />- ... in the Meeting Invite sent by the xxxx Epic Owner (i.e. Umut Sariskal / Christine Michaud) to our customer and xxxx</p></td><td><p><br /></p></td><td><p><br /></p><p>OK! xxxx target DNS CNAME .<a href="http://xxxxdns.net">xxxxdns.net</a> settings found.</p><p>&nbsp;<a href="http://WEB_DOMAIN">WEB_DOMAIN</a> &rarr; <a href="http://CNAME_WEB">CNAME_WEB</a><br /> <a href="http://API_DOMAIN">API_DOMAIN</a> &rarr; <a href="http://CNAME_API">CNAME_API</a></p><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="cnameWEB_DOMAIN.png" ac:width="370"><ri:attachment ri:filename="cnameWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="cnameAPI_DOMAIN.png" ac:width="370"><ri:attachment ri:filename="cnameAPI_DOMAIN.png" ri:version-at-save="1" /></ac:image><p>  </p></td><td><p><br /></p></td><td><p /></td></tr><tr><td><p><br /></p></td><td><p>&nbsp; SSL cert installation</p><p><em>Has the SSL certificate been uploaded by GSOC from VENAFI&nbsp;</em><br /><em>Is it valid?</em><br /><br /><br /><br /></p></td><td><p><br /></p></td><td><p>AIRLINE_TYPE: </p><p>DOMAIN_CERT</p><p /><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="certdataWEB_DOMAIN_2.png" ac:width="370"><ri:attachment ri:filename="certdataWEB_DOMAIN_2.png" ri:version-at-save="1" /></ac:image><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="certdataAPI_DOMAIN_2.png" ac:width="370"><ri:attachment ri:filename="certdataAPI_DOMAIN_2.png" ri:version-at-save="1" /></ac:image></td><td><p><br /></p></td><td><p /></td></tr><tr><td><p><br /></p></td><td><p><strong>OPTIONAL:</strong> SSL cert installation on the xx origin VIP<br /><br /><em>Does the Origin VIP SSL certificate match with the SSL certificate deployed on xxxx? (Expected: they should be exactly the same) </em><br /><br /><em>You must spoof your local hosts file:</em><br /><br /><em>&lt;Origin VIP&gt; &lt;domain name&gt;</em></p></td><td><p><br /></p></td><td><p>Ok VIRTUAL_IP_0 </p><p>HTTP_RESPONSE_HEADER</p><p>OK - The origin SSL cert is a SAN cert that contains the</p><p>&nbsp;Subject Alternative Names:</p><p>CERT_DATA_WEB</p><p>OK - The origin SSL cert is valid (not expired).</p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="720" ac:original-width="1280" ac:width="408"><ri:attachment ri:filename="domaintext_0_img.png" ri:version-at-save="1" /></ac:image></td><td><p><br /></p></td><td><p /></td></tr><tr><td><p><strong><u>Pre2</u></strong></p><p>White List Checking</p></td><td><p>Define as per standard recommendation<br />(done by GSOC team Olivier Thonnard / Clemence Guay / Shruti Suman / Bindhu Shree through TR)</p><p><br />&rarr; Validation step TO BE REMOVED as it is handled by GSOC before the ABP activation in BLOCKING mode</p></td><td><p><br /></p></td><td><p><br /></p></td><td><p>N/A<br /><br /><br /><br /></p></td><td><p /></td></tr><tr><td><p><strong><u>Pre3</u></strong></p><p>URL hostname and DNS Checking</p></td><td><p><strong><u>1.&nbsp;In Apache config </u></strong><br />AeRE legacy: e-commerce dashboard<br /><br /><br />AeRE Praxis : <br /><br />DES&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;Web domain&gt;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;API domain&gt;</p><p>&rarr; Validation sub-step TO BE REVIEWED if NEEDED<br /><br /><br /></p><p><strong><u>2. xxxx external DNS checking</u></strong></p><p>Expected result: the xxxx DNS (*.<a href="http://xxxxdns.net">xxxxdns.net</a>) should be reachable.<br />this step is also intended to ensure there are no <em>typos / misspellings </em>in the DNS. <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p><p><em>&rarr; Validation sub-step NEEDED</em></p></td><td><p><br /></p></td><td><p>???</p><p><strong>2. </strong></p><p>OK &ndash; the xxxx DNS domain is valid (resolves to an IP within CIDR range).</p><p>$ ping <a href="http://CNAME_WEB">CNAME_WEB</a></p><p><ac:image ac:original-height="40" ac:original-width="800" ac:inline="true"><ri:attachment ri:filename="pingCNAME_WEB.png" ri:version-at-save="1" /></ac:image> </p><p>$ ping <a href="http://CNAME_API">CNAME_API</a></p><p><ac:image ac:original-height="40" ac:original-width="800" ac:inline="true"><ri:attachment ri:filename="pingCNAME_API.png" ri:version-at-save="1" /></ac:image> </p></td><td><p>OK</p></td><td><p /></td></tr><tr><td><p><strong><u>Pre4</u></strong></p><p>IP Checking</p></td><td><p><strong><u>Ping Airline URL</u></strong></p><p>Expected result: The DNS record SHOULD be already created &ndash; targeting xxxx.<br /><br /></p><p>Use <strong>ping</strong> command.<br /><em>Note 1: ICMP protocol traffic might be disabled on the destination IP firewall (so this is expected behavior).</em></p><p><br /></p></td><td><p><br /></p></td><td><p>OK &ndash; the DNS record is already created &ndash; targeting xxxx.</p><p>$ping <a href="http://WEB_DOMAIN">WEB_DOMAIN</a></p><p><ac:image ac:original-height="40" ac:original-width="800" ac:inline="true"><ri:attachment ri:filename="pingWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image> </p><p>$ping <a href="http://API_DOMAIN">API_DOMAIN</a></p><p><ac:image ac:original-height="40" ac:original-width="800" ac:inline="true"><ri:attachment ri:filename="pingAPI_DOMAIN.png" ri:version-at-save="1" /></ac:image>  </p><p>Complementary check: use &quot;dig&quot; command:</p><p>$ dig +noall +answer <a href="http://WEB_DOMAIN">WEB_DOMAIN</a></p><p>$ dig +noall +answer <a href="http://API_DOMAIN">API_DOMAIN</a></p></td><td><p /></td><td><p>OK</p></td></tr><tr><td><p><strong><u>Pre5</u></strong></p><p>DNS Checking</p></td><td><p><strong><u>On Jump server</u></strong></p><p>URL not created yet</p><p>Result:</p><p><em>N/A </em><br /><br /><em>&rarr; Validation step TO BE REVIEWED. Still relevant ??</em></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p>N/A</p></td><td><p /></td></tr><tr><td><p><strong><u>Pre6</u></strong></p><p>Traffic Checking</p></td><td><p><strong><u>OPNet:</u></strong><br />New URL (Web): <a href="https://muconp06.cws.xxxx.net/">https://muconp06.cws.xxxx.net/</a><br />Old URL: <a href="https://muconp03.os.xxxx.net:8443/home.jsp">https://muconp03.os.xxxx.net:8443/home.jsp</a></p><p>Search the VIP. Is it available?</p><p><br /></p></td><td><p><br /></p></td><td><p><br /></p><p>Yes, IP can be found in OPNET (helpful to monitor real time traffic reaching xx web domain):</p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="720" ac:original-width="1280" ac:width="408"><ri:attachment ri:filename="trafficflow_img.png" ri:version-at-save="1" /></ac:image></td><td><p>OK</p></td><td><p /></td></tr><tr><td><p><br /></p></td><td><p><strong><u>Sentinel</u></strong></p><p>Traffic visible on JCP Sentinel</p></td><td><p><br /></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p /></td></tr><tr><td><p><strong><u>Pre7</u></strong></p><p>Emulate traffic through xxxx</p></td><td><p><strong><u>STEP 7.1: Spoofing the host file with the xxxx IP</u></strong><br /><br /><strong># Spoofing - Traffic through xxxx </strong><br /><strong>&lt;IP_address_of_xxxx&gt; &lt;domain&gt; </strong></p><p><br />&lt;IP_address_of_xxxx&gt; to be spoofed with, to reach xxxx, can be found by running a <strong>ping to the xxxx.</strong><a href="http://incapdns.net"><strong>incapdns.net</strong></a><strong> CNAME. </strong><br /><br /><em>Expected behavior:</em></p><p><u>Before &ndash; N/A</u></p><p>URL not created yet</p><p><u>&nbsp;</u></p><p><u>After:</u></p><p>Flow is going through xxxx platform.<br /></p><p><strong><u>STEP 7.2: Flow through xxxx</u></strong><br /><br />Expected behavior: </p><p>Observe in Developer Tools <br />- InitConfig and Webhooks flows shows, in the Remote IP, the right xxxx IP <br /><br />&nbsp; (but be careful, it might be unreliable and misleading, due to the Netskope plugin/service/daemon enforcing the <em>actual</em> DNS resolution! See help on the cell &quot;Help&quot;).&nbsp; </p><p>- 100% reliable check: make sure the Response Header contains <strong>x-cdn: xxxx</strong>. <br />&nbsp;&nbsp; If yes, then it means your test URL went through xxxx platform. If not, we are not going yet through xxxx.<br /><br />- 100% reliable check: make sure that you can see the JS of xxxx JavaScript:<br />&nbsp;&nbsp;</p><p>Traffic in xxxx Portal</p><p>Apache log check \uf0e0 N/A (only possible on JCP farms)</p><p /><p>Checked in Apache log (IP X.X.X.X is my IP):</p><p><br />And the results are in the below ALF log link. Got my true client IP for my sanity checks. All good from my end.&nbsp;</p><p><a href="API_LOG">API_LOG</a></p><p>Web domain:</p><p><a href="SPLUNK_URL">Splunk_logs</a></p></td><td><p><em>Note that as part of the <strong><u>xxxx onboarding:</u></strong></em></p><p><em><strong>A.</strong> If the airline will NOT implement their own CDN in front of xxxx:</em></p><ul><li><p><em>&rarr; The DNS change will be done by the customer during the On-boarding, to make it target xxxx.</em></p></li></ul><p><em><strong>B. </strong>If the airline will implement their own CDN in front of xxxx:</em></p><ul><li><p><em>&rarr; The CDN &quot;Origin setting&quot; change will be done by the customer during the On-boarding, </em><br /><em>to make it forward the traffic to xxxx.</em></p></li></ul><p><em>Either way, the simulation that the traffic can&nbsp;go via xxxx can be achieved via hosts file spoofing.</em><br /><br />&nbsp;You may need to disconnect from the Cisco AnyConnect VPN to make the hosts file to work.</p><p>&nbsp;You may need to disable&nbsp;<em>temporarily</em> NETSKOPE (formerly it was Bluecoat) plugin and service/daemon to make the hosts file spoofing to work. <br />Remember we are not supposed to disable Netskope as they are intended to protect your laptop</p></td><td><p>1. Find the IPs to spoof to reach xxxx:</p><p>$ ping <a href="http://CNAME_WEB">CNAME_WEB</a></p><p><ac:image ac:original-height="40" ac:original-width="800" ac:inline="true"><ri:attachment ri:filename="pingCNAME_WEB.png" ri:version-at-save="1" /></ac:image> </p><p>$ ping <a href="http://CNAME_API">CNAME_API</a></p><p><ac:image ac:original-height="40" ac:original-width="800" ac:inline="true"><ri:attachment ri:filename="pingCNAME_API.png" ri:version-at-save="1" /></ac:image>  </p><p>2. Host file spoofing:</p><p>Spoofing - Traffic through xxxx:</p><p>45.60.124.29 <a href="http://WEB_DOMAIN">WEB_DOMAIN</a> </p><p>45.60.124.29 <a href="http://API_DOMAIN">API_DOMAIN</a> <br /></p><p>3. Run the flow and verify that traffic went via xxxx, checking HTTP response headers (do not trust the IP) OK - x-cdn: xxxx found in HTTP Response header.</p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="720" ac:original-width="1280" ac:width="408"><ri:attachment ri:filename="domaintext_1_img.png" ri:version-at-save="1" /></ac:image></td><td><p>&nbsp;Partially Edgeproxy-cip is missing in ALF logs.</p></td><td><p /></td></tr><tr><td><p><strong><u>Pre8</u></strong></p><p>Redirection checking</p></td><td><p><u>Booking URL access must be redirected to the Airline portal </u>AeRE DX customers (and only certain DDS customers)</p><p>Apache redirection confirmed <br /><br /><sub>&rarr; Normally this validation item is not needed since xxxx supports quite well POST form resubmit after CAPTCHA is solved. </sub><br /><sub>In the past when it was not supported by DistilNetworks, after solving a CAPTCHA the user was redirected to the domain root path (</sub><a href="https://book.airlinename.com)"><sub>https://book.airlinename.com)</sub></a><sub> which in turn was redirected by our Apache rule to the web portal (</sub><a href="https://www.airlinename.com)"><sub>https://www.airlinename.com)</sub></a></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p>OK</p></td><td><p /></td></tr><tr><td><p><strong><u>OTHER</u></strong></p></td><td><p><strong><u>&nbsp;</u></strong></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p /></td></tr></tbody></table><p><br /></p>'
    # Confluence template only for web domain.
    
    web_template = '<h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:local-id="bfb9d815-bd1f-49af-bef0-55bd619c4dec" ac:macro-id="5658bb63-055e-4065-9630-2f2f67fcceab"><ac:parameter ac:name="">scroll-bookmark-1</ac:parameter></ac:structured-macro><span style="color: rgb(23,43,77);">This is the Validation TR for:</span></h1><ac:structured-macro ac:name="unmigrated-wiki-markup" ac:schema-version="1" data-layout="default" ac:local-id="491dae03-06aa-490e-a6b1-deb95fbe4d8c" ac:macro-id="26681243-ea60-437b-8c94-efe914c2f8d5"><ac:plain-text-body><![CDATA[*TR_TITLE* \n*+Pre-requisites:+*]]></ac:plain-text-body></ac:structured-macro><ul><li><p>Access to xxxx Cloud WAF console (provided by GSOC team - POC Shruti SUMAN / Mohamed FANGAR): <br /><a href="https://my.xxxx.com/admin/login">https://my.xxxx.com/admin/login</a></p></li><li><p>Have installed dig command (on Windows: BIND <a href="https://www.isc.org/download/">download</a> link)</p></li></ul><table data-table-width="1800" data-layout="full-width" ac:local-id="99425094-5712-4066-b468-5855d4dc246f"><colgroup><col style="width: 359.0px;" /><col style="width: 359.0px;" /><col style="width: 359.0px;" /><col style="width: 386.0px;" /><col style="width: 332.0px;" /></colgroup><tbody><tr><td><p><strong>Steps</strong></p></td><td><p><strong>Expected result&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </strong></p></td><td><p><strong>Help</strong></p></td><td><p><strong>Activity Status</strong></p></td><td><p><strong>Status</strong></p></td></tr><tr><td><p><strong><u>Pre1</u></strong></p><p>xxxx Configuration Checking</p></td><td><p><u>On the xxxx admin portal / Edit Settings</u><br /><br /><u>xxxx web portal:</u></p><p>&nbsp; Is domain defined on the xxxx console?</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Yes, domain exists</p></td><td><p><br /></p></td><td><p><a href="http://WEB_DOMAIN">WEB_DOMAIN</a> </p><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="domainWEB_DOMAIN.png" ac:width="371"><ri:attachment ri:filename="domainWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><p /></td><td><p>OK<br /><br /><br /></p></td></tr><tr><td><p><br /></p></td><td><p>&nbsp; Do the Origin DNSs exist?</p><p><em>Make sure the Origin CNAME(s) domain is/are well setup: </em></p><p><br /><em>AERE (1 domain): Typically </em><br /><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </em><a href="http://origin-xxxxx.xxxx.com"><em>origin-xxxxx.xxxx.com</em></a> <br /><br /><em>DES (2 domains): Typically: </em><br /><em>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; origin-xx&lt;product&gt;-</em><a href="http://web.xxxx.com"><em>web.xxxx.com</em></a> &nbsp;&nbsp;&nbsp;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>digital touchpoints. &lt;airline name&gt;.</em><a href="http://airlines.api.xxxx.com"><em>airlines.api.xxxx.com</em></a></p></td><td><p>Website settings &gt; Origin servers<br /><br /><br />Website settings &gt; General</p></td><td><p>ORIGIN_EXISTS<br />AIRLINE_TYPE: </p><p>&lt;Origin_web_domain&gt;:  <a href="http://WEB_ORIGIN">WEB_ORIGIN</a>   </p><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="originWEB_DOMAIN.png" ac:width="371"><ri:attachment ri:filename="originWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><p /></td><td><p><br /></p></td></tr><tr><td><p><br /></p></td><td><p><strong><u>xxxx WAF portal:</u></strong> <br />All parameters are configured in BLOCKING mode</p></td><td><p>Website settings &gt;<br />WAF<br /><br /><br />SERVICES &gt; WAF &gt; WAF Policies</p></td><td><p><br /></p><p>DDOS for web domain set to automatic.</p></td><td><p><br /></p></td></tr><tr><td><p><br /></p></td><td><p>Review xxxx target DNS CNAME settings. <br /><br />Then, make sure they MATCH with the settings mentioned...<br />- ... in the Task Record <br />- ... in the Meeting Invite sent by the xxxx Epic Owner (i.e. Umut Sariskal / Christine Michaud) to our customer and xxxx</p></td><td><p><br /></p></td><td><p><br /></p><p>OK! xxxx target DNS CNAME .<a href="http://xxxxdns.net">xxxxdns.net</a> settings found.</p><p>&nbsp;<a href="http://WEB_DOMAIN">WEB_DOMAIN</a> &rarr; <a href="http://CNAME_WEB">CNAME_WEB</a><br /></p><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="cnameWEB_DOMAIN.png" ac:width="371"><ri:attachment ri:filename="cnameWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><p /><p>  </p></td><td><p><br /></p></td></tr><tr><td><p><br /></p></td><td><p>&nbsp; SSL cert installation</p><p><em>Has the SSL certificate been uploaded by GSOC from VENAFI&nbsp;</em><br /><em>Is it valid?</em><br /><br /><br /><br /></p></td><td><p><br /></p></td><td><p>AIRLINE_TYPE: </p><p>DOMAIN_CERT</p><ac:image ac:align="center" ac:layout="center" ac:original-height="864" ac:original-width="1536" ac:custom-width="true" ac:alt="certdataWEB_DOMAIN_2.png" ac:width="371"><ri:attachment ri:filename="certdataWEB_DOMAIN_2.png" ri:version-at-save="1" /></ac:image><p /></td><td><p><br /></p></td></tr><tr><td><p><br /></p></td><td><p><strong>OPTIONAL:</strong> SSL cert installation on the xx origin VIP<br /><br /><em>Does the Origin VIP SSL certificate match with the SSL certificate deployed on xxxx? (Expected: they should be exactly the same) </em><br /><br /><em>You must spoof your local hosts file:</em><br /><br /><em>&lt;Origin VIP&gt; &lt;domain name&gt;</em></p></td><td><p><br /></p></td><td><p>Ok VIRTUAL_IP_0</p><p>HTTP_RESPONSE_HEADER</p><p>OK - The origin SSL cert is a SAN cert that contains the</p><p>&nbsp;Subject Alternative Names:</p><p>CERT_DATA_WEB</p><p>OK - The origin SSL cert is valid (not expired).</p><ac:image ac:align="center" ac:layout="center" ac:original-height="2250" ac:original-width="4000" ac:custom-width="true" ac:alt="domaintext_0_img.png" ac:width="371"><ri:attachment ri:filename="domaintext_0_img.png" ri:version-at-save="1" /></ac:image><p /></td><td><p><br /></p></td></tr><tr><td><p><strong><u>Pre2</u></strong></p><p>White List Checking</p></td><td><p>Define as per standard recommendation<br />(done by GSOC team Olivier Thonnard / Clemence Guay / Shruti Suman / Bindhu Shree through TR)</p><p><br />&rarr; Validation step TO BE REMOVED as it is handled by GSOC before the ABP activation in BLOCKING mode</p></td><td><p><br /></p></td><td><p><br /></p></td><td><p>N/A<br /><br /><br /><br /></p></td></tr><tr><td><p><strong><u>Pre3</u></strong></p><p>URL hostname and DNS Checking</p></td><td><p><strong><u>1.&nbsp;In Apache config </u></strong><br />AeRE legacy: e-commerce dashboard<br /><br /><br />AeRE Praxis : <br /><br />DES&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;Web domain&gt;</p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &lt;API domain&gt;</p><p>&rarr; Validation sub-step TO BE REVIEWED if NEEDED<br /><br /><br /></p><p><strong><u>2. xxxx external DNS checking</u></strong></p><p>Expected result: the xxxx DNS (*.<a href="http://xxxxdns.net">xxxxdns.net</a>) should be reachable.<br />this step is also intended to ensure there are no <em>typos / misspellings </em>in the DNS. <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p><p><em>&rarr; Validation sub-step NEEDED</em></p></td><td><p><br /></p></td><td><p>???</p><p><strong>2. </strong></p><p>OK &ndash; the xxxx DNS domain is valid (resolves to an IP within CIDR range).</p><p>$ ping <a href="http://CNAME_WEB">CNAME_WEB</a></p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="40" ac:original-width="800" ac:width="408"><ri:attachment ri:filename="pingCNAME_WEB.png" ri:version-at-save="1" /></ac:image></td><td><p>OK</p></td></tr><tr><td><p><strong><u>Pre4</u></strong></p><p>IP Checking</p></td><td><p><strong><u>Ping Airline URL</u></strong></p><p>Expected result: The DNS record SHOULD be already created &ndash; targeting xxxx.<br /><br /></p><p>Use <strong>ping</strong> command.<br /><em>Note 1: ICMP protocol traffic might be disabled on the destination IP firewall (so this is expected behavior).</em></p><p><br /></p></td><td><p><br /></p></td><td><p>OK &ndash; the DNS record is already created &ndash; targeting xxxx.</p><p>$ping <a href="http://WEB_DOMAIN">WEB_DOMAIN</a></p><ac:image ac:align="center" ac:layout="center" ac:original-height="32" ac:original-width="640" ac:custom-width="true" ac:alt="pingWEB_DOMAIN.png" ac:width="371"><ri:attachment ri:filename="pingWEB_DOMAIN.png" ri:version-at-save="1" /></ac:image><p /><p>Complementary check: use &quot;dig&quot; command:</p><p>$ dig +noall +answer <a href="http://WEB_DOMAIN">WEB_DOMAIN</a></p></td><td><p>OK</p></td></tr><tr><td><p><strong><u>Pre5</u></strong></p><p>DNS Checking</p></td><td><p><strong><u>On Jump server</u></strong></p><p>URL not created yet</p><p>Result:</p><p><em>N/A </em><br /><br /><em>&rarr; Validation step TO BE REVIEWED. Still relevant ??</em></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p>N/A</p></td></tr><tr><td><p><strong><u>Pre6</u></strong></p><p>Traffic Checking</p></td><td><p><strong><u>OPNet:</u></strong><br />New URL (Web): <a href="https://muconp06.cws.xxxx.net/">https://muconp06.cws.xxxx.net/</a><br />Old URL: <a href="https://muconp03.os.xxxx.net:8443/home.jsp">https://muconp03.os.xxxx.net:8443/home.jsp</a></p><p>Search the VIP. Is it available?</p><p><br /></p></td><td><p><br /></p></td><td><p><br /></p><p>Yes, IP can be found in OPNET (helpful to monitor real time traffic reaching xx web domain):</p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="720" ac:original-width="1280" ac:width="408"><ri:attachment ri:filename="trafficflow_img.png" ri:version-at-save="1" /></ac:image></td><td><p>OK</p></td></tr><tr><td><p><br /></p></td><td><p><strong><u>Sentinel</u></strong></p><p>Traffic visible on JCP Sentinel</p></td><td><p><br /></p></td><td><p><br /></p></td><td><p><br /></p></td></tr><tr><td><p><strong><u>Pre7</u></strong></p><p>Emulate traffic through xxxx</p></td><td><p><strong><u>STEP 7.1: Spoofing the host file with the xxxx IP</u></strong><br /><br /><strong># Spoofing - Traffic through xxxx </strong><br /><strong>&lt;IP_address_of_xxxx&gt; &lt;domain&gt; </strong></p><p><br />&lt;IP_address_of_xxxx&gt; to be spoofed with, to reach xxxx, can be found by running a <strong>ping to the xxxx.</strong><a href="http://incapdns.net"><strong>incapdns.net</strong></a><strong> CNAME. </strong><br /><br /><em>Expected behavior:</em></p><p><u>Before &ndash; N/A</u></p><p>URL not created yet</p><p><u>&nbsp;</u></p><p><u>After:</u></p><p>Flow is going through xxxx platform.<br /></p><p><strong><u>STEP 7.2: Flow through xxxx</u></strong><br /><br />Expected behavior: </p><p>Observe in Developer Tools <br />- InitConfig and Webhooks flows shows, in the Remote IP, the right xxxx IP <br /><br />&nbsp; (but be careful, it might be unreliable and misleading, due to the Netskope plugin/service/daemon enforcing the <em>actual</em> DNS resolution! See help on the cell &quot;Help&quot;).&nbsp; </p><p>- 100% reliable check: make sure the Response Header contains <strong>x-cdn: xxxx</strong>. <br />&nbsp;&nbsp; If yes, then it means your test URL went through xxxx platform. If not, we are not going yet through xxxx.<br /><br />- 100% reliable check: make sure that you can see the JS of xxxx JavaScript:<br />&nbsp;&nbsp;</p><p>Traffic in xxxx Portal</p><p>Apache log check \uf0e0 N/A (only possible on JCP farms)</p><p /><p>Checked in Apache log (IP X.X.X.X is my IP):</p><p><br />And the results are in the below ALF log link. Got my true client IP for my sanity checks. All good from my end.&nbsp;</p><p><a href="API_LOG">API_LOG_URL</a></p><p>Web domain:</p><p><a href="SPLUNK_URL">Splunk_log</a></p></td><td><p><em>Note that as part of the <strong><u>xxxx onboarding:</u></strong></em></p><p><em><strong>A.</strong> If the airline will NOT implement their own CDN in front of xxxx:</em></p><ul><li><p><em>&rarr; The DNS change will be done by the customer during the On-boarding, to make it target xxxx.</em></p></li></ul><p><em><strong>B. </strong>If the airline will implement their own CDN in front of xxxx:</em></p><ul><li><p><em>&rarr; The CDN &quot;Origin setting&quot; change will be done by the customer during the On-boarding, </em><br /><em>to make it forward the traffic to xxxx.</em></p></li></ul><p><em>Either way, the simulation that the traffic can&nbsp;go via xxxx can be achieved via hosts file spoofing.</em><br /><br />&nbsp;You may need to disconnect from the Cisco AnyConnect VPN to make the hosts file to work.</p><p>&nbsp;You may need to disable&nbsp;<em>temporarily</em> NETSKOPE (formerly it was Bluecoat) plugin and service/daemon to make the hosts file spoofing to work. <br />Remember we are not supposed to disable Netskope as they are intended to protect your laptop</p></td><td><p>1. Find the IPs to spoof to reach xxxx:</p><p>$ ping <a href="http://CNAME_WEB">CNAME_WEB</a></p><ac:image ac:align="left" ac:layout="align-start" ac:original-height="40" ac:original-width="800" ac:width="408"><ri:attachment ri:filename="pingCNAME_WEB.png" ri:version-at-save="1" /></ac:image><p /><p>2. Host file spoofing:</p><p>Spoofing - Traffic through xxxx:</p><p>45.60.124.29 <a href="http://WEB_DOMAIN">WEB_DOMAIN</a> <br /></p><p>3. Run the flow and verify that traffic went via xxxx, checking HTTP response headers (do not trust the IP) OK - x-cdn: xxxx found in HTTP Response header.</p><ac:image ac:align="center" ac:layout="center" ac:original-height="2250" ac:original-width="4000" ac:custom-width="true" ac:alt="domaintext_1_img.png" ac:width="371"><ri:attachment ri:filename="domaintext_1_img.png" ri:version-at-save="1" /></ac:image><p /></td><td></td></tr><tr><td><p><strong><u>Pre8</u></strong></p><p>Redirection checking</p></td><td><p><u>Booking URL access must be redirected to the Airline portal </u>AeRE DX customers (and only certain DDS customers)</p><p>Apache redirection confirmed <br /><br /><sub>&rarr; Normally this validation item is not needed since xxxx supports quite well POST form resubmit after CAPTCHA is solved. </sub><br /><sub>In the past when it was not supported by DistilNetworks, after solving a CAPTCHA the user was redirected to the domain root path (</sub><a href="https://book.airlinename.com)"><sub>https://book.airlinename.com)</sub></a><sub> which in turn was redirected by our Apache rule to the web portal (</sub><a href="https://www.airlinename.com)"><sub>https://www.airlinename.com)</sub></a></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p>OK</p></td></tr><tr><td><p><strong><u>OTHER</u></strong></p></td><td><p><strong><u>&nbsp;</u></strong></p></td><td><p><br /></p></td><td><p><br /></p></td><td><p><br /></p></td></tr></tbody></table><p><br /></p>'

    # Read data and config yaml files.
    dom_data = md.readYaml('data.yaml')
    config_data = md.readYaml('config.yaml')

    # Generate custom templates.
    if len(config_data['dom_test']) == 1 and 'api' not in str(config_data['dom_test']):
        globals()['cust_template'] = web_template.replace('TR_TITLE', dom_data['tr_title']).replace('WEB_DOMAIN',
                                                                                                    dom_data[
                                                                                                        'web_domain']).replace(
            'AIRLINE_TYPE', config_data['airline_type']).replace('WEB_ORIGIN', dom_data['web_origin']).replace(
            'CNAME_WEB', dom_data['cname_web']).replace('SPLUNK_URL',
                                                        dom_data['splunk_url'].replace(r'&', '&amp;')).replace(
            'ORIGIN_EXISTS', 'Ok origin exists for this airline domain.').replace('DDOS_SETTING', 'DDOS for web domain set to automatic.').replace(
            'DOMAIN_CERT', 'Ok web domain has installed with the same SAN SSL cert (or wildcard SSL cert) as the one installed on the F5.').replace(
            'VIRTUAL_IP_0', dom_data['virtual_ip_0']).replace('HTTP_RESPONSE_HEADER', 'HTTP response header: lack of x-cdn: xxxx is an indicator that the origin has been reached directly.').replace(
            'CERT_DATA_WEB', dom_data['cert_data_web']).replace('API_LOG', dom_data['api_log'])

    else:
        cust_template = web_api_template.replace('TR_TITLE', dom_data['tr_title']).replace('WEB_DOMAIN', dom_data[
            'web_domain']).replace('API_DOMAIN', dom_data['api_domain']).replace('AIRLINE_TYPE',
                                                                                 config_data['airline_type']).replace(
            'WEB_ORIGIN', dom_data['web_origin']).replace('API_ORIGIN', dom_data['api_origin']).replace('CNAME_WEB',
                                                                                                        dom_data[
                                                                                                            'cname_web']).replace(
            'CNAME_API', dom_data['cname_api']).replace('SPLUNK_URL',
                                                        dom_data['splunk_url'].replace(r'&', '&amp;')).replace(
            'ORIGIN_EXISTS', 'Ok origin exists for this airline domain.').replace('DDOS_SETTING', 'DDOS for both web and api domains set to automatic.').replace(
            'DOMAIN_CERT', 'Ok both web and api domains have installed with the same SAN SSL cert (or wildcard SSL cert) as the one installed on the F5.').replace(
            'VIRTUAL_IP_0', dom_data['virtual_ip_0']).replace('HTTP_RESPONSE_HEADER', 'HTTP response header: lack of x-cdn: xxxx is an indicator that the origin has been reached directly.').replace(
            'CERT_DATA_WEB', dom_data['cert_data_web'])

    # Call to generate confluence report.
    Confluence_wiki.update_confluence(cust_template)

