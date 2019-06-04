# from selenium.webdriver.chrome import webdriver
from time import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# options.add_experimental_option("prefs", {
#         "download.default_directory": r"C:\temp",
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing.enabled": True
# })

driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)


def get_full_url(num):
    return 'https://codewithmosh.com/courses/complete-sql-mastery/lectures/' + str(num)


def get_course_name_and_page_id_map():
    return ["10143091|1-1- Introduction",
            "9590090|1-2- What is SQL",
            "9590091|1-3- Installing MySQL on Mac",
            "9590089|1-4- Installing MySQL on Windows",
            "9590092|1-5- Creating the Databases",
            "10143042|1-6- What You ll Learn",
            "9590114|2-1- The SELECT Statement",
            "9590110|2-2- The SELECT Clause",
            "9590107|2-3- The WHERE Clause",
            "9590116|2-4- The AND, OR and NOT Operators",
            "9590112|2-5- The IN Operator",
            "9590113|2-6- The BETWEEN Operator",
            "9590108|2-7- The LIKE Operator",
            "9590111|2-8- The REGEXP Operator",
            "9590115|2-9- The IS NULL Operator",
            "9590109|2-10- The ORDER BY Clause",
            "9590117|2-11- The LIMIT Clause",
            "9590157|3-1- Inner Joins",
            "9590159|3-2- Joining Across Databases",
            "9590152|3-3- Self Joins",
            "9590163|3-4- Joining Multiple Tables",
            "9590161|3-5- Compound Join Conditions",
            "9590158|3-6- Implicit Join Syntax",
            "9590155|3-7- Outer Joins",
            "9590154|3-8- Outer Join Between Multiple Tables",
            "9590153|3-9- Self Outer Joins",
            "9590162|3-10- The USING Clause",
            "9590164|3-11- Natural Joins",
            "9590160|3-12- Cross Joins",
            "9590156|3-13- Unions",
            "9590180|4-1- Column Attributes",
            "9590183|4-2- Inserting a Row",
            "9590182|4-3- Inserting Multiple Rows",
            "9590188|4-4- Inserting Hierarchical Rows",
            "9590187|4-5- Creating a Copy of a Table",
            "9590185|4-6- Updating a Single Row",
            "9590179|4-7- Updating Multiple Rows",
            "9590186|4-8- Using Subqueries in Updates",
            "9590181|4-9- Deleting Rows",
            "9590184|4-10- Restoring the Databases",
            "9590223|5-1- Aggregate Functions",
            "9590220|5-2- The GROUP BY Clause",
            "9590222|5-3- The HAVING Clause",
            "9590221|5-4- The ROLLUP Operator",
            "9590240|6-1- Introduction",
            "9590237|6-2- Subqueries",
            "9590235|6-3- The IN Operator",
            "9590241|6-4- Subqueries vs Joins",
            "9590248|6-5- The ALL Keyword",
            "9590246|6-6- The ANY Keyword",
            "9590242|6-7- Correlated Subqueries",
            "9590236|6-8- The EXISTS Operator",
            "9590238|6-9- Subqueries in the SELECT Clause",
            "9590239|6-10- Subqueries in the FROM Clause",
            "9590264|7-1- Numeric Functions",
            "9590262|7-2- String Functions",
            "9590261|7-3- Date Functions in MySQL",
            "9590266|7-4- Formatting Dates and Times",
            "9590267|7-5- Calculating Dates and Times",
            "9590263|7-6- The IFNULL and COALESCE Functions",
            "9590265|7-7- The IF Function",
            "9590268|7-8- The CASE Operator",
            "9590280|8-1- Creating Views",
            "9590284|8-2- Altering or Dropping Views",
            "9590281|8-3- Updatable Views",
            "9590283|8-4- THE WITH OPTION CHECK Clause",
            "9590282|8-5- Other Benefits of Views",
            "9590329|9-1- What are Stored Procedures",
            "9590330|9-2- Creating a Stored Procedure",
            "9590333|9-3- Creating Procedures Using MySQLWorkbench",
            "9590331|9-4- Dropping Stored Procedures",
            "9590334|9-5- Parameters",
            "9590337|9-6- Parameters with Default Value",
            "9590335|9-7- Parameter Validation",
            "9590338|9-8- Output Parameters",
            "9590332|9-9- Variables",
            "9590340|9-10- Functions",
            "9590336|9-11- Other Conventions",
            "9707196|10-1- Triggers",
            "9707200|10-2- Viewing Triggers",
            "9707201|10-3- Dropping Triggers",
            "9707199|10-4- Using Triggers for Auditing",
            "9707198|10-5- Events",
            "9707197|10-6- Viewing, Dropping and Altering Events",
            "9710684|11-1- Transactions",
            "9710690|11-2- Creating Transactions",
            "9710683|11-3- Concurrency and Locking",
            "9710689|11-4- Concurrency Problems",
            "9710687|11-5- Transaction Isolation Levels",
            "9710688|11-6- READ UNCOMMITTED Isolation Level",
            "9710691|11-7- READ COMMITTED Isolation Level",
            "9710685|11-8- REPEATABLE READ Isolation Level",
            "9710686|11-9- SERIALIZABLE Isolation Level",
            "9710692|11-10- Deadlocks",
            "9780497|12-1- Introduction",
            "9780500|12-2- String Types",
            "9780492|12-3- Integer Types",
            "9780494|12-4- Fixed-point and Floating-point Types",
            "9780498|12-5- Boolean Types",
            "9780499|12-6- Enum and Set Types",
            "9780495|12-7- Date and Time Types",
            "9780496|12-8- Blob Types",
            "9780493|12-9- JSON Type",
            "9880339|13-1- Introduction",
            "9880355|13-2- Data Modelling",
            "9880358|13-3- Conceptual Models",
            "9880364|13-4- Logical Models",
            "9880361|13-5- Physical Models",
            "9880352|13-6- Primary Keys",
            "9880351|13-7- Foreign Keys",
            "9880366|13-8- Foreign Key Constraints",
            "9880353|13-9- Normalization",
            "9880348|13-10- 1NF- First Normal Form",
            "9880360|13-11- Link Tables",
            "9880354|13-12- 2NF- Second Normal Form",
            "9880342|13-13- 3NF- Third Normal Form",
            "9880345|13-14- My Pragmatic Advice",
            "9880344|13-15- Dont Model the Universe",
            "9880338|13-16- Forward Engineering a Model",
            "9880350|13-17- Synchronizing a Model with a Database",
            "9880356|13-18- Reverse Engineering a Database",
            "9880362|13-19- Project- Flight Booking System",
            "9880346|13-20- Solution- Conceptual Model",
            "9880363|13-21- Solution- Logical Model",
            "9880368|13-22- Project - Video Rental Application",
            "9880340|13-23- Solution- Conceptual Model",
            "9880367|13-24- Solution- Logical Model",
            "9880347|13-25- Creating and Dropping Databases",
            "9880365|13-26- Creating Tables",
            "9880343|13-27- Altering Tables",
            "9880349|13-28- Creating Relationships",
            "9880357|13-29- Altering Primary and Foreign Key Constraints",
            "9880341|13-30- Character Sets and Collations",
            "9880359|13-31- Storage Engines",
            "10096054|14-1- Introduction",
            "10096055|14-2- Indexes",
            "10096058|14-3- Creating Indexes",
            "10096061|14-4- Viewing Indexes",
            "10096056|14-5- Prefix Indexes",
            "10096060|14-6- Full-text Indexes",
            "10096059|14-7- Composite Indexes",
            "10096051|14-8- Order of Columns in Composite Indexes",
            "10096062|14-9- When Indexes are Ignored",
            "10096052|14-10- Using Indexes for Sorting",
            "10096053|14-11- Covering Indexese",
            "10096050|14-12- Index Maintenance",
            "10108074|15-1- Introduction",
            "10108075|15-2- Creating a User",
            "10108081|15-3- Viewing Users",
            "10108080|15-4- Dropping Users",
            "10108079|15-5- Changing Passwords",
            "10108076|15-6- Granting Privileges",
            "10108078|15-7- Viewing Privileges",
            "10108077|15-8- Revoking Privileges",
            "10142300|15-9- Wrap Up",
            ]


def test():
    [get_each_page(item.split('|')) for item in get_course_name_and_page_id_map()]


def get_each_page(item):
    driver.get(get_full_url(item[0]))
    download = driver.find_element_by_css_selector('a.download')
    print(item[0])
    print(download.get_attribute('href'))


def get_download_script(id, filename):
    return f'''
    return fetch('https://www.filepicker.io/api/file/{id}',
        {{
            "credentials": "same-origin",
            "referrerPolicy": "no-referrer-when-downgrade",
            "body": null,
            "method": "GET",
            "mode": "cors"
        }}
    ).then(resp => {{
        return resp.blob();
    }}).then(blob => {{
        saveAs(blob, '{filename}');
    }});
    '''


def main():
    driver.maximize_window()
    driver.execute_script("""(function(a,b){if("function"==typeof define&&define.amd)define([],b);else if("undefined"!=typeof exports)b();else{b(),a.FileSaver={exports:{}}.exports}})(this,function(){"use strict";function b(a,b){return"undefined"==typeof b?b={autoBom:!1}:"object"!=typeof b&&(console.warn("Deprecated: Expected third argument to be a object"),b={autoBom:!b}),b.autoBom&&/^\s*(?:text\/\S*|application\/xml|\S*\/\S*\+xml)\s*;.*charset\s*=\s*utf-8/i.test(a.type)?new Blob(["\uFEFF",a],{type:a.type}):a}function c(b,c,d){var e=new XMLHttpRequest;e.open("GET",b),e.responseType="blob",e.onload=function(){a(e.response,c,d)},e.onerror=function(){console.error("could not download file")},e.send()}function d(a){var b=new XMLHttpRequest;b.open("HEAD",a,!1);try{b.send()}catch(a){}return 200<=b.status&&299>=b.status}function e(a){try{a.dispatchEvent(new MouseEvent("click"))}catch(c){var b=document.createEvent("MouseEvents");b.initMouseEvent("click",!0,!0,window,0,0,0,80,20,!1,!1,!1,!1,0,null),a.dispatchEvent(b)}}var f="object"==typeof window&&window.window===window?window:"object"==typeof self&&self.self===self?self:"object"==typeof global&&global.global===global?global:void 0,a=f.saveAs||("object"!=typeof window||window!==f?function(){}:"download"in HTMLAnchorElement.prototype?function(b,g,h){var i=f.URL||f.webkitURL,j=document.createElement("a");g=g||b.name||"download",j.download=g,j.rel="noopener","string"==typeof b?(j.href=b,j.origin===location.origin?e(j):d(j.href)?c(b,g,h):e(j,j.target="_blank")):(j.href=i.createObjectURL(b),setTimeout(function(){i.revokeObjectURL(j.href)},4E4),setTimeout(function(){e(j)},0))}:"msSaveOrOpenBlob"in navigator?function(f,g,h){if(g=g||f.name||"download","string"!=typeof f)navigator.msSaveOrOpenBlob(b(f,h),g);else if(d(f))c(f,g,h);else{var i=document.createElement("a");i.href=f,i.target="_blank",setTimeout(function(){e(i)})}}:function(a,b,d,e){if(e=e||open("","_blank"),e&&(e.document.title=e.document.body.innerText="downloading..."),"string"==typeof a)return c(a,b,d);var g="application/octet-stream"===a.type,h=/constructor/i.test(f.HTMLElement)||f.safari,i=/CriOS\/[\d]+/.test(navigator.userAgent);if((i||g&&h)&&"object"==typeof FileReader){var j=new FileReader;j.onloadend=function(){var a=j.result;a=i?a:a.replace(/^data:[^;]*;/,"data:attachment/file;"),e?e.location.href=a:location=a,e=null},j.readAsDataURL(a)}else{var k=f.URL||f.webkitURL,l=k.createObjectURL(a);e?e.location=l:location.href=l,e=null,setTimeout(function(){k.revokeObjectURL(l)},4E4)}});f.saveAs=a.saveAs=a,"undefined"!=typeof module&&(module.exports=a)});
""")

    driver.get("https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1")

    user_email = driver.find_element_by_id('user_email')
    user_email.send_keys('rayzrchen@gmail.com')

    user_password = driver.find_element_by_id('user_password')
    user_password.send_keys('Hsbc1234')
    user_password.send_keys(Keys.ENTER)

    # [get_each_page(item.split('|')) for item in get_course_name_and_page_id_map()]
    # driver.get('https://www.filepicker.io/api/file/wePUPergTeeOoETUKyrD')
    driver.execute_script(get_download_script('wePUPergTeeOoETUKyrD', '1.mp4'))

    driver.close()


main()
# test()

