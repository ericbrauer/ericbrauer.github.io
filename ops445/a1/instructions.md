<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="generator" content="pandoc">
  <meta name="author" content="Eric Brauer">
  <title>Assignment 1 Winter 2024</title>
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, minimal-ui">
  <link rel="stylesheet" href="https://unpkg.com/reveal.js@^4//dist/reset.css">
  <link rel="stylesheet" href="https://unpkg.com/reveal.js@^4//dist/reveal.css">
  <style>
    .reveal .sourceCode {  /* see #7635 */
      overflow: visible;
    }
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    span.underline{text-decoration: underline;}
    div.column{display: inline-block; vertical-align: top; width: 50%;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    ul.task-list{list-style: none;}
    pre > code.sourceCode { white-space: pre; position: relative; }
    pre > code.sourceCode > span { display: inline-block; line-height: 1.25; }
    pre > code.sourceCode > span:empty { height: 1.2em; }
    .sourceCode { overflow: visible; }
    code.sourceCode > span { color: inherit; text-decoration: inherit; }
    div.sourceCode { margin: 1em 0; }
    pre.sourceCode { margin: 0; }
    @media screen {
    div.sourceCode { overflow: auto; }
    }
    @media print {
    pre > code.sourceCode { white-space: pre-wrap; }
    pre > code.sourceCode > span { text-indent: -5em; padding-left: 5em; }
    }
    pre.numberSource code
      { counter-reset: source-line 0; }
    pre.numberSource code > span
      { position: relative; left: -4em; counter-increment: source-line; }
    pre.numberSource code > span > a:first-child::before
      { content: counter(source-line);
        position: relative; left: -1em; text-align: right; vertical-align: baseline;
        border: none; display: inline-block;
        -webkit-touch-callout: none; -webkit-user-select: none;
        -khtml-user-select: none; -moz-user-select: none;
        -ms-user-select: none; user-select: none;
        padding: 0 4px; width: 4em;
        color: #aaaaaa;
      }
    pre.numberSource { margin-left: 3em; border-left: 1px solid #aaaaaa;  padding-left: 4px; }
    div.sourceCode
      {   }
    @media screen {
    pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
    }
    code span.al { color: #ff0000; font-weight: bold; } /* Alert */
    code span.an { color: #60a0b0; font-weight: bold; font-style: italic; } /* Annotation */
    code span.at { color: #7d9029; } /* Attribute */
    code span.bn { color: #40a070; } /* BaseN */
    code span.bu { color: #008000; } /* BuiltIn */
    code span.cf { color: #007020; font-weight: bold; } /* ControlFlow */
    code span.ch { color: #4070a0; } /* Char */
    code span.cn { color: #880000; } /* Constant */
    code span.co { color: #60a0b0; font-style: italic; } /* Comment */
    code span.cv { color: #60a0b0; font-weight: bold; font-style: italic; } /* CommentVar */
    code span.do { color: #ba2121; font-style: italic; } /* Documentation */
    code span.dt { color: #902000; } /* DataType */
    code span.dv { color: #40a070; } /* DecVal */
    code span.er { color: #ff0000; font-weight: bold; } /* Error */
    code span.ex { } /* Extension */
    code span.fl { color: #40a070; } /* Float */
    code span.fu { color: #06287e; } /* Function */
    code span.im { color: #008000; font-weight: bold; } /* Import */
    code span.in { color: #60a0b0; font-weight: bold; font-style: italic; } /* Information */
    code span.kw { color: #007020; font-weight: bold; } /* Keyword */
    code span.op { color: #666666; } /* Operator */
    code span.ot { color: #007020; } /* Other */
    code span.pp { color: #bc7a00; } /* Preprocessor */
    code span.sc { color: #4070a0; } /* SpecialChar */
    code span.ss { color: #bb6688; } /* SpecialString */
    code span.st { color: #4070a0; } /* String */
    code span.va { color: #19177c; } /* Variable */
    code span.vs { color: #4070a0; } /* VerbatimString */
    code span.wa { color: #60a0b0; font-weight: bold; font-style: italic; } /* Warning */
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <link rel="stylesheet" href="https://unpkg.com/reveal.js@^4//dist/theme/black.css" id="theme">
  <link rel="stylesheet" href="css/custom.css"/>
</head>
<body>
  <div class="reveal">
    <div class="slides">

<section id="title-slide">
  <h1 class="title">Assignment 1 Winter 2024</h1>
  <p class="author">Eric Brauer</p>
</section>

<section>
<section id="instructions-group-assignment-winter-2024"
class="title-slide slide level1">
<h1>Instructions: Group Assignment Winter 2024</h1>

</section>
<section id="overview" class="slide level2">
<h2>Overview</h2>
<p>You are going to be creating a <strong>budget planning tool</strong>.
When your script is run with a starting date and an ending date, it will
print a <strong>calendar output</strong> similar to the <code>cal</code>
utility. After printing the calendar output, your script will prompt the
user for some information, and return some budget information.</p>
<p>Sample Output:</p>
<pre><code>$ python3 ./assignment1.py 01/01/2024 18/04/2024

    January 2024    
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31         

   February 2024    
Su Mo Tu We Th Fr Sa
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29      

     March 2024     
Su Mo Tu We Th Fr Sa
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31                  

     April 2024     
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18      

How much do you make per pay period? $5000
How much is your monthly rent? $2000

Report for 01/01/2024 to 18/04/2024
====================================
Number of workdays:   78
Number of weekends:   30

Number of paycheques:    8
Amount for each paycheque: $5000.00

Number of times rent is due:    3

Total pay: $40000.00
Total rent: $6000.00
Net: $34000.00</code></pre>
</section>
<section id="requirements" class="slide level2">
<h2>Requirements</h2>
<ul>
<li>Command line arguments required: start date, end date in DD/MM/YYYY
format</li>
<li>If start date is later than end date, your code should select the
latest date as end date</li>
<li>Use after() function to iterate through the dates</li>
<li>Write a function (or functions) to generate calendar output for all
the dates in the range</li>
<li>Use <code>input()</code> to ask for pay and rent amounts</li>
<li>Count number of weekdays and weekend days</li>
<li>For this exercise, assume that a payday happens on the <strong>first
and third thursday of every month</strong></li>
<li>Rent is due (I’m sure you’re aware!) on the first of each month</li>
<li>Print totals for all paydays and for all rent due days</li>
<li>Include a net income/shortfall at the end of the output</li>
</ul>
</section>
<section id="restrictions" class="slide level2">
<h2>Restrictions</h2>
<ul>
<li>You may <strong>only use <code>sys</code> for parsing command line
arguments</strong></li>
<li>No other modules are allowed</li>
<li><strong>Use only code that you’ve learned in the course.</strong>
Code that is outside the scope of the course, maybe be flagged for
revision</li>
</ul>
</section>
<section id="this-is-a-group-project" class="slide level2">
<h2>This Is A Group Project</h2>
<ul>
<li>I will assign groups of 4-5 students</li>
<li>Each group will be committing to one repository</li>
<li>It is up to you how you want to organize the workload, but</li>
<li>each student will be partly graded on their commits to the repo</li>
</ul>
</section>
<section id="instructions" class="slide level2">
<h2>Instructions</h2>
<p>The assignment will be broken into one milestone and one final
submission. Please update your repository for each milestone and
complete the final submission in order to earn all marks.</p>
<ul>
<li>Milestone 1 will be due on <strong>February 9, 2024</strong>.</li>
<li>The Final submission will be due on <strong>March 8,
2024</strong>.</li>
<li>The PostMortem document and Revisions will be due on <strong>March
15, 2024</strong></li>
</ul>
</section>
<section class="slide level2">

<h3 id="preparation">Preparation</h3>
<ol type="1">
<li>You will be assigned a group and a shared repository.</li>
<li>Accept the assignment on Blackboard.</li>
<li>Add your code to the <em>existing</em> <code>assignment1.py</code>
file.</li>
<li>Commit after <strong>each significant change</strong> to the
code.</li>
<li><strong>You can never have too many commits.</strong> GitHub is your
proof of work and your backup if things go wrong.</li>
</ol>
<h3 id="milestone-1">Milestone 1</h3>
<p>You are provided with a function called <code>after()</code>. This
function is complete and should successfully return the next day’s date
when provided with a starting date in <code>DD/MM/YYYY</code> format.
You can experiment with this function by importing it into the Python
interpreter:</p>
<div class="sourceCode" id="cb2"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> assignment1 <span class="im">import</span> after</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>after(<span class="st">&#39;25/01/2023&#39;</span>)</span></code></pre></div>
<p>Use your understanding of <code>after()</code> to create <em>in-line
comments</em> for the <code>after()</code> function and the other
functions below.</p>
<p>This Milestone will also ask you to <em>refactor</em> your code. This
means modifying existing code to make it more portable.</p>
<ol type="1">
<li>Complete the <code>leap_year()</code> function, using the relevant
code that’s already inside <code>after()</code>.</li>
<li>Edit your <code>after()</code> function. Replace any code that
calculates leap years with a <code>leap_year</code> function call.<br />
</li>
<li>Repeat the same process for the <code>mon_max()</code>
function.</li>
<li>Verify that <code>after()</code> still works after your
changes.</li>
<li>Complete the <code>valid_date()</code> function. This should use
error checking to make sure that any date entered by the user is valid.
A valid year is any year between <strong>1538 and 2999</strong>.</li>
</ol>
<p>Finally, you are asked to <strong>provide a plan for your calendar
function</strong>. This can included inside <code>assignment1.py</code>
as a <em>docstring</em>, or you can choose to add an
<code>algorithm.txt</code> document to your repo.</p>
<ol type="1">
<li>What inputs will your function require (ie. arguments)?</li>
<li>Your function will need to print headers for the months. What
circumstances will trigger a print header?</li>
<li>Will your function require iteration? If so, a for loop, or a while
loop?</li>
<li>What circumstances will trigger a new row in your calendar?</li>
<li>What other functions will your calendar function call?</li>
</ol>
<p>Your algorithm should be written in clear, direct English. Use point
form to break the algorithm into steps. Pseudocode is recommended. Your
algorithm will be graded based on clarity, and attention to detail.
Grammar and spelling will not be considered, unless it impacts our
ability to understand your submission.</p>
<h4 id="check-your-work">Check Your Work</h4>
<p>Use the check script to verify your work so far.</p>
<ul>
<li><code>python3 checkA1.py -f -v TestAfter</code></li>
<li><code>python3 checkA1.py -f -v TestLeap</code></li>
<li><code>python3 checkA1.py -f -v TestMonMax</code></li>
<li><code>python3 checkA1.py -f -v TestValidDate</code></li>
</ul>
<p>Or run:</p>
<p><code>python3 checkA1.py -f -v</code></p>
<p>to test everything in one step.</p>
<h4 id="feedback">Feedback</h4>
<p>The week after Milestone is submitted, we will have a <strong>Code
Review</strong> meeting. In this meeting, you will be expected to
explain parts of your code, and some parts of your submission might be
<strong>flagged for revision</strong>. In this case you have until the
end of the week to push those revisions to earn your milestone
marks.</p>
<p>In addition, this is an excellent time to ask questions, and get
guidance on the next stage of the assignment.</p>
<h3 id="final-submission">Final Submission</h3>
<ul>
<li>Complete your calendar function.</li>
<li>Implement command line arguments, and verify that both are valid
dates. Print a usage message and quit if not.</li>
<li>Verify that <code>end_date</code> is later than
<code>start_date</code>, otherwise switch the values.</li>
<li>Complete code for the input prompts, and use another solution to
count weekdays, weekends, paydays and rent days. = Print the final
output.</li>
<li>Test your code, and add documentation.</li>
</ul>
<h4 id="final-checks">Final Checks</h4>
<p>There are no unit tests for this stage. You should test your code
manually.</p>
<ul>
<li>Does your code start with earlier date, and end with later
date?</li>
<li>Does your calendar print headers, and include both the start date
and end date?</li>
<li>Does your math make sense?</li>
<li>What happens when the user enters unexpected input?</li>
</ul>
<h4 id="submitting-your-code-for-review">Submitting Your Code For
Review</h4>
<ol type="1">
<li>Push your code to GitHub before the deadline.</li>
</ol>
<h3 id="postmortem-document">PostMortem Document</h3>
<ul>
<li>Each group is asked to submit a document afterwards, which is a
reflection on the assignment.</li>
<li>This document should be written in <strong>plain, direct
English</strong>. I’m not marking your grammar or spelling, but it needs
to be understandable.</li>
<li>This should be 1 - 2 pages in length, submitted as a docx file, to
Blackboard.</li>
<li>Respond to these prompts:
<ul>
<li>How did you organize group work? Was this a good approach? How will
you organize group work differently in the future?</li>
<li>What part of the assignment was the most challenging? What methods
did you use to solve problems?</li>
<li>Did all group members contribute to the assignment? How did you deal
with disagreements within the group?</li>
<li>What inputs did you use to test the final submission of your code?
How did you evaluate the output of your code?</li>
<li>Is there any part of the starting code or requirements that caused
challenges? How would you change your code if that requirement was taken
away?</li>
<li>Now that you have completed your assignment, are there any useful
applications / modifications that you can think of? How could you use
this assignment as a starting point for creating something useful and
relevant to your own life?</li>
</ul></li>
</ul>
<h3 id="revisions">Revisions</h3>
<p>You may be required to complete revisions to your final submission.
Code that is flagged for revision includes any code that is <strong>out
of scope for the course</strong>. The deadline for revisions will be
decided by the instructor. Revisions must be complete for the assignment
to be considered complete.</p>
</section>
<section id="formatting-and-style" class="slide level2">
<h2>Formatting And Style</h2>
<p>A significant amount of your mark will be based on the things that
<em>aren’t</em> your code. Please review the following guidelines to
maximise your grade.</p>
<h3 id="comments-and-documentation">Comments And Documentation</h3>
<p><strong>You need to be commenting your code</strong>. The following
documentation is required:</p>
<ul>
<li><strong>in-line comments</strong>: Any line of code that is doing
something non-obvious should be commented. Explain <strong>why</strong>
you are doing something, rather than <strong>what</strong> you are
doing.</li>
<li><strong>function docstrings</strong>: After your <code>def</code>
line, you enter a docstring inside ““. Any function that doesn’t already
come with a docstring should have one.</li>
<li><strong>top-level docstring</strong>: You will have noticed that the
top of your <code>assignment1.py</code> file already has this docstring.
Complete the <strong>Academic Honesty declaration</strong> and complete
the docstring.</li>
</ul>
<h3 id="pep">PEP</h3>
<p>The <a href="https://peps.python.org/pep-0008/">PEP-8 Style Guide</a>
is an official Python document that describes best practices for
formatting your code. <strong>You should follow this guide as much as
possible</strong>. You may find that <a
href="https://code.visualstudio.com/docs/python/linting">using a
linter</a> to check style to be useful.</p>
<h3 id="functions-and-variables">Functions and Variables</h3>
<ul>
<li><p>In addition to the required functions, you may create as many
functions as you need.</p></li>
<li><p>Functions should be in lower case, and spaces should be
represented with an underscore. For example:
<code>function_name</code>.</p></li>
<li><p>Any data used inside of a function should be passed in as a
parameter. Avoid global variables.</p></li>
<li><p>Variables should have a sensible name. Avoid naming things
<code>x</code>. Replace <code>x</code> with a more suitable
name.</p></li>
<li><p>Variables should be in lower case, and spaces represented by an
underscore. For example: <code>start_date</code>.</p></li>
</ul>
<h3 id="git-commits">Git Commits</h3>
<p>A workplace will have its own policy about how often to commit, and
how to document commits. For us, <strong>git commits are your proof of
work</strong>. Assignments that lack commits are subject to
<strong>Academic Integrity review</strong>.</p>
<ul>
<li>A good practice is to create a commit for <strong>every significant
change</strong> to your code. <strong>At the very least, commit after
completing each of the required functions.</strong></li>
<li>An acceptable commit message needs to short, but should also
describe the change. For example:
<code>git commit -m "completed the leap_year function"</code>.</li>
</ul>
</section>
<section id="sample-output" class="slide level2">
<h2>Sample Output</h2>
<h3 id="normal-function">Normal function</h3>
<p><strong>Note</strong>:
<code>How much do you make per pay period</code> and
<code>How much is your monthly rent</code> are <code>input()</code>
statements.</p>
<p><code>python3 ./assignment1.py 01/01/2024 14/01/2024</code></p>
<pre><code>    January 2024    
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14

How much do you make per pay period? $200
How much is your monthly rent? $400

Report for 01/01/2024 to 14/01/2024
====================================
Number of workdays:    9
Number of weekends:    4

Number of paycheques:    1
Amount for each paycheque: $200.00

Number of times rent is due:    0

Total pay: $200.00
Total rent: $0.00
Net: $200.00</code></pre>
<h3 id="arguments-reversed">Arguments Reversed</h3>
<p>Program swaps start date and end date automatically</p>
<p><code>python3 ./assignment1.py 14/01/2024 01/01/2024</code></p>
<pre><code>    January 2024    
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14

How much do you make per pay period? $200
How much is your monthly rent? $400

Report for 01/01/2024 to 14/01/2024
====================================
Number of workdays:    9
Number of weekends:    4

Number of paycheques:    1
Amount for each paycheque: $200.00

Number of times rent is due:    0

Total pay: $200.00
Total rent: $0.00
Net: $200.00</code></pre>
<h3 id="invalid-argument">Invalid Argument</h3>
<p><code>python3 ./assignment1.py 30/02/2024 20/04/2024</code></p>
<pre><code>Error: wrong day entered
Usage: ./assignment1.py DD/MM/YYYY DD/MM/YYYY</code></pre>
<h3 id="invalid-input">Invalid Input</h3>
<p><code>python3 ./assignment1.py 14/01/2024 01/01/2024</code></p>
<pre><code>    January 2024    
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14

How much do you make per pay period? $peanuts
Error: not a valid number
Exiting...</code></pre>
</section>
<section id="rubric" class="slide level2">
<h2>Rubric</h2>
<h3 id="first-milestone">First Milestone</h3>
<table>
<thead>
<tr class="header">
<th>Weight</th>
<th>Item</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>TestAfter Check</td>
</tr>
<tr class="even">
<td>3</td>
<td>TestLeap Check</td>
</tr>
<tr class="odd">
<td>3</td>
<td>TestMonMax Check</td>
</tr>
<tr class="even">
<td>3</td>
<td>TestValidDate Check</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Documentation</td>
</tr>
<tr class="even">
<td>5</td>
<td>Algorithm</td>
</tr>
<tr class="odd">
<td><strong>20</strong></td>
<td><strong>Total</strong></td>
</tr>
</tbody>
</table>
<h3 id="group">Group</h3>
<table>
<thead>
<tr class="header">
<th>Weight</th>
<th>Item</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>20</td>
<td>Milestone 1 (see above)</td>
</tr>
<tr class="even">
<td>2</td>
<td>error checking</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Code quality and style</td>
</tr>
<tr class="even">
<td>5</td>
<td>calendar output</td>
</tr>
<tr class="odd">
<td>5</td>
<td>day tracking (paydays, etc.)</td>
</tr>
<tr class="even">
<td>5</td>
<td>cost output</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Comments and Documentation</td>
</tr>
<tr class="even">
<td>10</td>
<td>Code Review</td>
</tr>
<tr class="odd">
<td>10</td>
<td>PostMortem Document</td>
</tr>
<tr class="even">
<td>5</td>
<td>GitHub Commit Quality</td>
</tr>
<tr class="odd">
<td><strong>70</strong></td>
<td><strong>Total</strong></td>
</tr>
</tbody>
</table>
<h3 id="individual">Individual</h3>
<p>Individual grade is based on your overall grade, and is modified
based on the following factors:</p>
<ul>
<li>Commits to the Codebase</li>
<li>Contributions during the code review meeting</li>
<li>Peer review during the postmortem</li>
</ul>
<table>
<thead>
<tr class="header">
<th>Weight</th>
<th>Item</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10</td>
<td>Commits</td>
</tr>
<tr class="even">
<td>10</td>
<td>Participation (Code Review)</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Peer Review</td>
</tr>
<tr class="even">
<td><strong>30</strong></td>
<td><strong>Total</strong></td>
</tr>
</tbody>
</table>
<p>In order to receive a decent individual mark, make sure your group’s
overall mark is high, and be sure to contribute your fair share to
overall efforts!</p>
</section></section>
    </div>
  </div>

  <script src="https://unpkg.com/reveal.js@^4//dist/reveal.js"></script>

  <!-- reveal.js plugins -->
  <script src="https://unpkg.com/reveal.js@^4//plugin/notes/notes.js"></script>
  <script src="https://unpkg.com/reveal.js@^4//plugin/search/search.js"></script>
  <script src="https://unpkg.com/reveal.js@^4//plugin/zoom/zoom.js"></script>

  <script>

      // Full list of configuration options available at:
      // https://revealjs.com/config/
      Reveal.initialize({
        // Display controls in the bottom right corner
        controls: true,

        // Help the user learn the controls by providing hints, for example by
        // bouncing the down arrow when they first encounter a vertical slide
        controlsTutorial: true,

        // Determines where controls appear, "edges" or "bottom-right"
        controlsLayout: 'bottom-right',

        // Visibility rule for backwards navigation arrows; "faded", "hidden"
        // or "visible"
        controlsBackArrows: 'faded',

        // Display a presentation progress bar
        progress: true,

        // Display the page number of the current slide
        slideNumber: false,

        // 'all', 'print', or 'speaker'
        showSlideNumber: 'all',

        // Add the current slide number to the URL hash so that reloading the
        // page/copying the URL will return you to the same slide
        hash: true,

        // Start with 1 for the hash rather than 0
        hashOneBasedIndex: false,

        // Flags if we should monitor the hash and change slides accordingly
        respondToHashChanges: true,

        // Push each slide change to the browser history
        history: false,

        // Enable keyboard shortcuts for navigation
        keyboard: true,

        // Enable the slide overview mode
        overview: true,

        // Disables the default reveal.js slide layout (scaling and centering)
        // so that you can use custom CSS layout
        disableLayout: false,

        // Vertical centering of slides
        center: true,

        // Enables touch navigation on devices with touch input
        touch: true,

        // Loop the presentation
        loop: false,

        // Change the presentation direction to be RTL
        rtl: false,

        // see https://revealjs.com/vertical-slides/#navigation-mode
        navigationMode: 'default',

        // Randomizes the order of slides each time the presentation loads
        shuffle: false,

        // Turns fragments on and off globally
        fragments: true,

        // Flags whether to include the current fragment in the URL,
        // so that reloading brings you to the same fragment position
        fragmentInURL: true,

        // Flags if the presentation is running in an embedded mode,
        // i.e. contained within a limited portion of the screen
        embedded: false,

        // Flags if we should show a help overlay when the questionmark
        // key is pressed
        help: true,

        // Flags if it should be possible to pause the presentation (blackout)
        pause: true,

        // Flags if speaker notes should be visible to all viewers
        showNotes: false,

        // Global override for autoplaying embedded media (null/true/false)
        autoPlayMedia: null,

        // Global override for preloading lazy-loaded iframes (null/true/false)
        preloadIframes: null,

        // Number of milliseconds between automatically proceeding to the
        // next slide, disabled when set to 0, this value can be overwritten
        // by using a data-autoslide attribute on your slides
        autoSlide: 0,

        // Stop auto-sliding after user input
        autoSlideStoppable: true,

        // Use this method for navigation when auto-sliding
        autoSlideMethod: null,

        // Specify the average time in seconds that you think you will spend
        // presenting each slide. This is used to show a pacing timer in the
        // speaker view
        defaultTiming: null,

        // Enable slide navigation via mouse wheel
        mouseWheel: false,

        // The display mode that will be used to show slides
        display: 'block',

        // Hide cursor if inactive
        hideInactiveCursor: true,

        // Time before the cursor is hidden (in ms)
        hideCursorTime: 5000,

        // Opens links in an iframe preview overlay
        previewLinks: false,

        // Transition style (none/fade/slide/convex/concave/zoom)
        transition: 'slide',

        // Transition speed (default/fast/slow)
        transitionSpeed: 'default',

        // Transition style for full page slide backgrounds
        // (none/fade/slide/convex/concave/zoom)
        backgroundTransition: 'fade',

        // Number of slides away from the current that are visible
        viewDistance: 3,

        // Number of slides away from the current that are visible on mobile
        // devices. It is advisable to set this to a lower number than
        // viewDistance in order to save resources.
        mobileViewDistance: 2,

        // reveal.js plugins
        plugins: [
          RevealNotes,
          RevealSearch,
          RevealZoom
        ]
      });
    </script>
    </body>
</html>
