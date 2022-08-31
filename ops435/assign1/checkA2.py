#!/usr/bin/env python3

import unittest
import os, sys, time
import subprocess
import glob
import hashlib
import urllib.request
import socket
import importlib


class TestHelp(unittest.TestCase):

    def get_a2_filename(self):
        filelist = glob.glob('./a2_*.py')
        try:
            filelist.remove('./a2_template.py')
        except:
            pass
        if len(filelist) == 1:
            return filelist[0]
        else:
            print("Error: can't find the a2_<myseneca>.py file!")
            print("You should have one file beginning in 'a2_' and")
            print("ending in '.py' besides the template.")
            print("Remove the extra files from the current directory")
            print("and use 'git status' to ensure that they are not ")
            print("being tracked by git.")
            raise FileNotFoundError

    def setUp(self):
        #self.filename = self.get_a2_filename()
        self.filename = 'assignment2.py'
        self.testfile = 'usage_data_file'

    maxDiff = None

    def test_argparse_help(self):
        "check the output of ur.py -h"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-h'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'Output of `a2.py -h` doesn\'t match what\'s expected. Make sure you\'ve added an option!)'
        self.assertIn('-t {daily,weekly}, --time', stdout.decode('utf-8'), msg=error_output)
        # TODO can they adapt argparse with another option? 1/1 point

class TestList(unittest.TestCase):

    def get_a2_filename(self):
        filelist = glob.glob('./a2_*.py')
        try:
            filelist.remove('./a2_template.py')
        except:
            pass
        if len(filelist) == 1:
            return filelist[0]
        else:
            print("Error: can't find the a2_<myseneca>.py file!")
            print("You should have one file beginning in 'a2_' and")
            print("ending in '.py' besides the template.")
            print("Remove the extra files from the current directory")
            print("and use 'git status' to ensure that they are not ")
            print("being tracked by git.")
            raise FileNotFoundError

    def setUp(self):
        #self.filename = self.get_a2_filename()
        self.filename = 'assignment2.py'
        self.testfile = 'usage_data_file'

    maxDiff = None
    def test_list_user_func(self):
        "parse_for_user returns list of users"
        f = open(self.testfile, 'r')
        output = f.read()
        testlist = output.split('\n')
        f.close()
        module_name = self.filename[:-3]
        mymodule = importlib.import_module(module_name)
        expected = ['asmith', 'cwsmith', 'rchan', 'tsliu2'] 
        error_msg = "Your `parse_for_user function isn't returning the expected output. Expected output is a list with usernames"
        self.assertEqual(expected, mymodule.parse_for_user(testlist), error_msg) 

    def test_list_user(self):
        "using -l user returns a nice table of users"
        "this includes the title and banner"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'user', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """User list for usage_data_file
=============================
asmith
cwsmith
rchan
tsliu2
"""
        return_code = p.wait()
        error_output = 'Your output of a2.py -l user <target> doesn\'t match what\'s expected. Make sure you\'re formatting the output correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)

    def test_list_hosts(self):
        "using -l host returns table of hosts"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'host', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Host list for usage_data_file
=============================
10.40.105.130
10.40.91.236
10.40.91.247
10.43.115.162
"""
        return_code = p.wait()
        error_output = 'Output of a2.py -l host doesn\'t match what\'s expected. Make sure you\'re formatting the output correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)

    def test_list_hosts_v(self):
        "using -l host -v return verbose table"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'host', self.testfile, '-v'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Files to be processed: usage_data_file
Type of args for files <class 'str'>
Host list for usage_data_file
=============================
10.40.105.130
10.40.91.236
10.40.91.247
10.43.115.162
"""
        return_code = p.wait()
        error_output = 'Output of a2.py -l host -v doesn\'t match what\'s expected. Make sure the --verbose option is working correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)

class TestDate(unittest.TestCase):

    def get_a2_filename(self):
        filelist = glob.glob('./a2_*.py')
        try:
            filelist.remove('./a2_template.py')
        except:
            pass
        if len(filelist) == 1:
            return filelist[0]
        else:
            print("Error: can't find the a2_<myseneca>.py file!")
            print("You should have one file beginning in 'a2_' and")
            print("ending in '.py' besides the template.")
            print("Remove the extra files from the current directory")
            print("and use 'git status' to ensure that they are not ")
            print("being tracked by git.")
            raise FileNotFoundError

    def setUp(self):
        #self.filename = self.get_a2_filename()
        self.filename = 'assignment2.py'
        self.testfile = 'usage_data_file'

    maxDiff = None
    # def test_list_user_func(self):
    #     "this will test function rather than output as a whole"
    #     f = open(self.testfile, 'r')
    #     output = f.read()
    #     testlist = output.split('\n')
    #     f.close()
    #     module_name = self.filename[:-3]
    #     mymodule = importlib.import_module(module_name)
    #     expected = ['asmith', 'cwsmith', 'rchan', 'tsliu2'] 
    #     error_msg = "Your `parse_for_user function isn't returning the expected output. Expected output is a list with usernames"
    #     self.assertEqual(expected, mymodule.parse_for_user(testlist, None), error_msg) 

    def test_list_user_date(self):
        "-l user -d 2018-02-14 returns one name"
        "this includes the title and banner"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'user', '-d', '2018-02-14', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """User list for usage_data_file
=============================
cwsmith
"""
        return_code = p.wait()
        error_output = 'Your output of a2.py -l user -d <target> doesn\'t match what\'s expected. Make sure you\'re formatting the output correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)

    def test_list_user_date2(self):
        "-l user -d 2018-02-15 returns two names"
        "this includes the title and banner"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'user', '-d', '2018-02-15', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """User list for usage_data_file
=============================
cwsmith
rchan
"""
        return_code = p.wait()
        error_output = 'Your output of a2.py -l user -d <target> doesn\'t match what\'s expected. Make sure you\'re formatting the output correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)
    def test_list_host_date(self):
        "check output of ur.py -l host -d <date> <target>"
        "this includes the title and banner"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'host', '-d', '2018-02-14', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Host list for usage_data_file
=============================
10.40.105.130
"""
        return_code = p.wait()
        error_output = 'Your output of a2.py -l host -d <target> doesn\'t match what\'s expected. Make sure you\'re formatting the output correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)
    
    def test_invalid_date(self):
        "check output of ur.py -l host -d with bad date"
        "this includes the title and banner"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-l', 'host', '-d', '2018-02-xx', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Date not recognized. Use YYYY-MM-DD format.
"""
        return_code = p.wait()
        error_output = 'Your output of a2.py -l host -d with bad date is wrong.Make sure you\'re formatting the output correctly!)'
        self.assertEqual(accepted_output, stdout.decode('utf-8'), msg=error_output)


class TestDaily(unittest.TestCase):

    def get_a2_filename(self):
        filelist = glob.glob('./a2_*.py')
        try:
            filelist.remove('./a2_template.py')
        except:
            pass
        if len(filelist) == 1:
            return filelist[0]
        else:
            print("Error: can't find the a2_<myseneca>.py file!")
            print("You should have one file beginning in 'a2_' and")
            print("ending in '.py' besides the template.")
            print("Remove the extra files from the current directory")
            print("and use 'git status' to ensure that they are not ")
            print("being tracked by git.")
            raise FileNotFoundError

    def setUp(self):
        #self.filename = self.get_a2_filename()
        self.filename = 'assignment2.py'
        self.testfile = 'usage_data_file'

    maxDiff = None

    def test_daily_user(self):
        "check output of -u <user> -t daily. should return HH:MM:SS"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-u', 'rchan', '-t', 'daily', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Daily Usage Report for rchan
============================
Date                Usage
13/02/2018        0:26:20
15/02/2018        0:33:00
Total             0:59:20
"""
        return_code = p.wait()
        stdout_decoded = stdout.decode('utf-8')
        stdout_test = stdout_decoded.split()
        expect_test = accepted_output.split()
        error_output = 'Your output doesn\'t match what\'s expected. If the previous test passed, check that omitting -s is returning HH:MM:SS'
        self.assertEqual(expect_test, stdout_test, msg=error_output)

    def test_daily_user_v(self):
        "check output of -u <user> -t daily -v. should return verbose"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-u', 'rchan', '-t', 'daily', self.testfile, '-v'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Files to be processed: usage_data_file
Type of args for files <class 'str'>
usage report for user: rchan
usage report type: daily
Daily Usage Report for rchan
============================
Date                Usage
13/02/2018        0:26:20
15/02/2018        0:33:00
Total             0:59:20
"""
        return_code = p.wait()
        stdout_decoded = stdout.decode('utf-8')
        stdout_test = stdout_decoded.split()
        expect_test = accepted_output.split()
        error_output = 'Using verbose with -t daily isn\'t producing correct output!)'
        self.assertEqual(expect_test, stdout_test, msg=error_output)
    
    def test_daily_remote(self):
        "check output of -r <ip> -t daily"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-r', '10.40.105.130', '-t', 'daily', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Daily Usage Report for 10.40.105.130
====================================
Date                Usage
14/02/2018        3:02:11
13/02/2018        2:12:49
Total             5:15:00
"""
        return_code = p.wait()
        stdout_decoded = stdout.decode('utf-8')
        stdout_test = stdout_decoded.split()
        expect_test = accepted_output.split()
        error_output = 'Output of -r <ip> -t daily doesn\'t match what\'s expected.'
        self.assertEqual(expect_test, stdout_test, msg=error_output)

class TestWeekly(unittest.TestCase):

    def get_a2_filename(self):
        filelist = glob.glob('./a2_*.py')
        try:
            filelist.remove('./a2_template.py')
        except:
            pass
        if len(filelist) == 1:
            return filelist[0]
        else:
            print("Error: can't find the a2_<myseneca>.py file!")
            print("You should have one file beginning in 'a2_' and")
            print("ending in '.py' besides the template.")
            print("Remove the extra files from the current directory")
            print("and use 'git status' to ensure that they are not ")
            print("being tracked by git.")
            raise FileNotFoundError

    def setUp(self):
        #self.filename = self.get_a2_filename()
        self.filename = 'assignment2.py'
        self.testfile = 'usage_data_file'

    maxDiff = None

    # def test_monthly_user_func(self):
    #     "check function for partial marks"
    #     f = open(self.testfile, 'r')
    #     output = f.read()
    #     testlist = output.split('\n')
    #     f.close()
    #     module_name = self.filename[2:-3]
    #     mymodule = importlib.import_module(module_name)
    #     expected = {"02/2018": 10931, "03/2018": 2280}
    #     error_msg = "Your parse_for_monthly function isn't returning the expected output."
    #     self.assertEqual(expected, mymodule.parse_for_monthly(testlist, 'cwsmith'), error_msg) 

    def test_weekly_user(self):
        "check output of -u cwsmit -t weekly"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-u', 'cwsmith', '-t', 'weekly', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Weekly Usage Report for cwsmith
===============================
Date                Usage
2018 06           3:02:11
2018 10           0:38:00
Total             3:40:11
"""
        return_code = p.wait()
        stdout_decoded = stdout.decode('utf-8')
        stdout_test = stdout_decoded.split()
        expect_test = accepted_output.split()
        error_output = 'check that -t weekly is returning correct output'
        self.assertEqual(expect_test, stdout_test, msg=error_output)

    def test_weekly_user_v(self):
        "check output of -u user -t weekly. should return HH:MM:SS -verbose"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-u', 'cwsmith', '-t', 'weekly', '-v', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Files to be processed: usage_data_file
Type of args for files <class 'str'>
usage report for user: cwsmith
usage report type: weekly
Weekly Usage Report for cwsmith
===============================
Date                Usage
2018 06           3:02:11
2018 10           0:38:00
Total             3:40:11
"""
        return_code = p.wait()
        stdout_decoded = stdout.decode('utf-8')
        stdout_test = stdout_decoded.split()
        expect_test = accepted_output.split()
        error_output = 'Your list output doesn\'t match what\'s expected. Make sure you\'re formatting the output correctly!)'
        self.assertEqual(expect_test, stdout_test, msg=error_output)
        
    def test_weekly_remote(self):
        "check output of -r <ip> -t weekly"
        p = subprocess.Popen(['/usr/bin/python3', self.filename, '-r', '10.43.115.162', '-t', 'weekly', self.testfile], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        accepted_output = """Weekly Usage Report for 10.43.115.162
=====================================
Date                Usage
2018 06           0:02:31
Total             0:02:31
""" 
        return_code = p.wait()
        stdout_decoded = stdout.decode('utf-8')
        stdout_test = stdout_decoded.split()
        expect_test = accepted_output.split()
        error_output = 'check that -t weekly is returning correct output'
        self.assertEqual(expect_test, stdout_test, msg=error_output)


def displayReportHeader():
    report_heading = 'OPS435 Lab Report - System Information for running '+sys.argv[0]
    print(report_heading)
    print(len(report_heading) * '=')
    print('    User login name:', os.getlogin())
    print('    Linux system version:', os.popen('cat /etc/redhat-release').read().strip())
    print('    Python executable:',sys.executable)
    print('    Python version: ',sys.version_info.major,sys.version_info.minor,sys.version_info.micro,sep='')
    print('    OS Platform:',sys.platform)
    print('    Working Directory:',os.getcwd())
    print('    Start at:',time.asctime())
    print(len(report_heading) * '=')
    return

def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'checkA2.py'
        lab_num = '~/a'
        print('Checking for updates...')
        if ChecksumLatest(url='https://ict.senecacollege.ca/~eric.brauer/ops435/ass/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for ' + lab_name + ' please consider updating:')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://ict.senecacollege.ca/~eric.brauer/ops435/ass/' + lab_name)
            print('Then run: git add ' +  lab_name)
            print('git commit -m "updated check script"')
            print('git push')
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return


if __name__ == '__main__':
    CheckForUpdates()
    # wait = input('Press ENTER to run the Lab Check...')
    if len(sys.argv) == 3:
        displayReportHeader()
    unittest.main()


