# sokkit
 The open source Sokkit static-hosting framework for Heroku.

# How to install on Heroku
 Download sokkit_server.py and the templates folder and add to your Heroku app. If you want, change the host, page name, and port.

# How to run the client
 Download sokkit_client.py. To use, run this command:
 `sokkit_client.py path/to/files last_digit_of_ip-host`
 You need to keep the client running, or users will be greeted with a 503 error.

# Directory structure
 Sokkit hosting directories must include:
* manifest.xml (Must include)
* other html files

# How to write an HTML file readable by Sokkit
 Sokkit only hosts HTML files, not the images, JS files, stylesheets, etc. in the project directory. Resources added over the Web are okay. One suggestion is uploading files to Google Drive and using them over the internet. Another is minifying all JS, CSS, or code, and converting smaller images to data URI's.

# manifest.xml syntax
 The main attribute is `<manifest>`. If you don't include it, an error will appear.
 Here's a sample:
```xml
<?xml version="1.0"?>
<manifest>
	<all>
		<path>/</path>
		<path>/foo</path>
		<path>/bar</path>
	</all>
	<pages>
		<page>
			<path>/</path>
			<filename>index.html</filename>
		</page>
		<page>
			<path>/foo</path>
			<filename>foo.html</filename>
		</page>
		<page>
			<path>/bar</path>
			<filename>bar.html</filename>
		</page>
	</pages>
</manifest>
```
where the `<all>` element is a list of all site paths. If you include a page in the `<pages>` section but do not add its path to the all section, you will get a 404 error. To add a path, type
```xml
<path>/sample_url</path>
```
. The `<pages>` section contains file paths in the project directory to all pages. To add a page, type
```xml
<page>
	<path>/sample_url</path>
	<filename>sample_file.html</filename>
</page>
```
 where path is the URL and filename is the file.

# Accessing pages
 To access pages on the site, the URL structure is `/site?path=/sample_url`.
