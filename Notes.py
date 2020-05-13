# Here are the three core topics we'll be covering in this lesson:
#
# 1. Interacting with a (remote) database
# Backend developers need to interact with databases on a regular basis in order to manipulate and maintain the models behind their web applications. In this lesson, we'll build a foundational understanding of how those interactions work.
#
# This foundational understanding will be essential in later lessons when we get into more advanced concepts related to database interactions.
#
# In working with a database, we'll need to use a Database Management System (DBMS).
#
# A Database Management System (DBMS) is simply software that allows you to interact with a database (e.g., to access or modify the data in that database).
#
# There are many different Database Management Systems out there, but the particular DBMS we'll be using is called PostgreSQL (or simply Postgres).
#
# 2. Database Application Programming Interfaces (DBAPIs)
# Once we've looked at the basics of interacting with a database, we'll need to understand how to interface with that database from another language or web server framework (such as Python, NodeJS, Ruby on Rails, etc.). This is where DBAPIs come in.
#
# In this lesson, we'll go over the basics of DBAPIs, and how they are used to interact with a database from another language (like Python).
#
# 3. psycopg2
# Finally, we'll get some experience working with the widely used psycopg2 library, which will allow us to interact with a database from Python.
#
# psycopg2 is a database adapter that allows us to interact with a Postgres database from Python.

# Takeaways
# # Primary Key
# # The primary key is the unique identifier for the entire row, referring to one or more columns.
# # If there are more multiple columns for the primary key, then the set of primary key columns is known as a composite key.
# # Foreign Key
# # A primary key in another (foreign) table.
# # Foreign keys are used to map relationships between tables.

# Inner joins between two tables returns rows of data that exist across all joined tables, excluding rows that may only
# exist in one of the tables but not the other table.
#
# Outer joins return every row that exists in the left (in a left outer join) or right (in a right outer join) joined
# table, while rendering NULL values on rows whose foreign key does not match a record in the other (right or left) table.
#
# The "left" table refers to the table to the left of the JOIN statement in the query, whereas the "right" table refers
# to the table to the right of the JOIN statement in the query.

# Client-Server Model
# In order to build database-backed web applications, we first need to understand how servers, clients, and databases interact.
#
# A major part of this is the client-server model, so let's look at that first. The basic idea is very simple, and looks ' \
#                                                        'something like this:
#
# A diagram showing the basic client-server model.
# A server is a centralized program that communicates over a network (such as the Internet) to serve clients.
#
# And a client is a program (like the web browser on your computer) that can request data from a server.
#
# When you go to a web page in your browser, your browser (the client) makes a request to the server—which then returns the data for that page.
#
# Adding databases to the model
# So that's the basic client-server model. But when you add in databases, this creates a little more complexity.
#
# In this next video, we'll review the basic model and then see how databases fit into things.

# In summary, relational database systems follow a client-server model:
#
# Servers, Clients, Hosts
# In a Client-Server Model, a server serves many clients.
# Servers and clients are programs that run on hosts.
# Hosts are computers connected over a network (like the internet!).
# Requests and Responses
# A client sends a request to the server
# The server's job is to fulfill the request with a response it sends back to the client.
# Requests and responses are served via a communication protocol, which sets up the expectations and rules for how the
#     communication occurs between servers and clients.
# Relational Database Clients
# A database client is any program that sends requests to a database
# In some cases, the database client is a web server! When your browser makes a request, the web server acts as a server
# (fulfilling that request), but when the web server requests data from the database, it is acting as a client to that
# database—and the database is the server (because it is fulfilling the request).
# Don't let this confuse you. Basically, we call things clients when they are making a request and servers when they are ' \
#    'fulfilling a request. Since a web server can do both, it sometimes acts as a server and sometimes acts as a client.

# Takeaways
# Clicking on the Polo product leads to a click event being registered by the browser, on the client computer.
# A click handler in the view would send a request to the server (in Javascript) from the client browser.
# A client could request more data and a different view to be rendered (with that data).
# A server process listens to the request sent from the view. It fetches the data and chooses what to render next,
# using the fetched data.
#
# Takeaways
# The client sends a request to the server, including information about the request type and any user input data.
# The server receives the request, and uses the user input data to determine how to shape its request to the database,
# and sends a request to the database.
# The database processes this request, and sends a response back to the web server.
# The server receives the response from the database, and uses it to determine the view + powers the view template with
#     the fetched data, sending it back to the client's browser.
# The client is responsible for rendering something to the user, that represents both the data and its representation.

# The web server receives a request from the client and sends a request to the database, which sends back a response to
# the web server*, which then sends back a response to the client**

# TCP/IP
# In this section, we'll look at the suite of communication protocols that is used to transfer data over the Internet. ' \
#                    'These communication protocols are most often referred to as TCP/IP, which is an abbreviation that ' \
#                    'refers to the two main protocols involved—Transmission Control Protocol (TCP) and Internet Protocol ' \
#                    '(IP).

# Takeaways
# TCP/IP is a suite of communication protocols that is used to connect devices and transfer data over the Internet.
#
# TCP/IP uses:
#
# IP addresses: An IP address identifies the location of a computer on a network.
# Ports: A port is a location on the recipient computer, where data is received.
# While an IP address tells you where to find a particular computer, it doesn't tell you specifically where on that ' \
#                                                                            'computer a particular connection should ' \
#                                                                            'be made—that's what port numbers are for.
#
# Some port numbers you should know:
#
# Port 80: The port number most commonly used for HTTP requests. For example, when a client makes a request to a
# web server, this request is usually sent through port 80.
# Port 5432: The port number used by most database systems; default port for Postgres.
#
# Correct!
#
# Ports allow multiple types of traffic being received at the same time on a given device, to be tracked and routed to
# where they need to go.
#
# Ports are much like the different terminals of an airport, tracking and receiving different airplanes at the same time,
# allowing for the effective receipt of multiple types of traffic at the same IP address.

# Correct!
#
# An IP address has many ports. In fact, there are a total of 65,535 TCP ports on a given computer—ranging
# from number 0 to 65535!

# Takeaways
# TCP/IP is connection-based, meaning all communications between parties are arranged over a connection. A connection is
# established before any data transmission begins.
# Over TCP/IP, we'll always need to establish a connection between clients and servers in order to enable communications. ' \
#                'Moreover:
# Deliveries over the connection are error-checked: if packets arrive damaged or lost, then they are resent (known as
# retransmission).
# Connecting starts a session. Ending the connection ends the session.
# In a database session, many transactions can occur during a given session. Each transaction does work to commit changes
# to the database (updating, inserting, or deleting records).
# Aside: the UDP Protocol
# The internet also offers the UDP protocol. UDP is much simpler than TCP: hosts on the network send data (in units called
# datagrams) without any connections needing to be established.

# TCP vs UDP
# If TCP is like building highways between houses before sending packages between them, then UDP is much like sending over
# a carrier pigeon from one house to another in order to deliver packages: you don't know whether the pigeon will head in ' \
#                                                                                 'the right way, drop your package along ' \
#                                                                                 'the way, or encounter an issue mid-travel. ' \
#                                                                                 'On the other hand, there is less overhead ' \
#                                                                                 'to use UDP than managing a connection over T' \
#                                                                                 'CP / building a highway.
#
# When speed is more important than reliability, especially when applications need to stream very small amounts of
# information quickly (smaller packages of information means less issues with reliability), then UDP is preferred.
# A lot of real time streaming applications, (e.g. live TV streaming, Voice over IP (VoIP)) prefer UDP over TCP.
# Since UDP does not need to retransmit lost datagrams, nor does it do any connection setup, there are fewer delays over
# UDP than TCP. TCP's continuous connection is more.

# a transaction captures one or more changes to a database, executed in order. A transaction either succeeds altogether,
# or fails altogether as a single unit. A transaction bundles multiple pieces of work into a single unit.

# Transactions capture operations that change a database's data: this means updates, inserts, and deletions of data. (UPDATE, ' \
#                                                      'INSERT, DELETE). Transactions are not concerned with querying ' \
#                                                      '(SELECT, GROUP BY) or changes to the data schema (ALTER TABLE)
#
# Changes to the database must be committed to the database by executing a commit to the transaction, after changes are
# queued into the transaction by adding to it.

# One can clear the queue of operations added to a transaction by doing a rollback.

# Initial installation settings
# The initial installation will:
#
# create an initial database named postgres
# create an initial user named postgres. Your postgres user will have no password set by default.
# create initial databases called template1 and template0. Any other database created after template1 is a clone of
# template1, including its tables and rows. If you add rows (objects) to template1, they will be copied onto future
# created databases. template0, on the other hand, should stay "pure" and never be changed.
# The default host machine that runs your postgres server, on your machine, is localhost (aka, 127.0.0.1)
# The default port traditionally used to host your server is port 5432. There are very few reasons to use a different port
# than 5432.
# Default connection settings are:
#
# Field	Default Value
# Host	localhost
# Port	5432
# Username	postgres
# Password	(left blank)
#

# Let's deep dive into what Postgres is
# Postgres is an open source, general purpose and object-relational database management system, considered by many to be
# the most advanced open source database system available. It's a relational database system extended with object-oriented ' \
#                                                            'features, that works across operating systems.
# Object-relational support includes support for arrays (multiple valuesin a single column), and inheritance (child-parent
# relationships between tables).
# Built since 1977, it is lauded for being highly stable, requiring minimal effort to maintain compared to other systems.
# Widely used, everywhere: by Apple, Cisco, Etsy, Microsoft, Yahoo, Reddit, Instagram, Uber,... and many others.
# Comprehensive suport for the SQL standard.
# Transaction-based: operations on the database are done through atomic transactions.
# Has multi-version concurrency control, avoiding unnecessary locking when multiple writes are happening to the database
# at once (avoiding waiting times for access to the database)
# Postgres lets you have several databases available for reading from and writing to, at once.
# Offers great performance and many indexing capabilities for optimizing query performance
#
# PostgreSQL is also often just called Postgres, and we'll be using both terms interchangeably throughout this course.

# Postgres CLI tools
# Keep this as a general reference. You'll be using these commands quite a lot if you are building web apps with Postgres.
#
# Log in as a particular user
# Default installed user is called postgres
#
# sudo -u <username> -i
# e.g. sudo -u bob -i
#
# Create a new database
# createdb <database_name>
# e.g. createdb mydb
#
# Destroy a database
# dropdb <database_name>
# e.g. dropdb mydb
#
# Reset a database
# dropdb <database_name> && createdb <database_name>
# e.g. dropdb mydb && createdb mydb

# Takeaways
# psql is an interactive terminal application for connecting and interacting with your local postgres server on your machine.
# Connect using $ psql <dbname>
# psql lets you
# Directly type and execute SQL commands to your database
# Inspect and preview your database and database tables using psql meta-commands
# Protip: type \? into psql to see a list of available commands
# Useful basic psql commands
# psql <dbname> [<username>]
#
# Starts psql with a connection to dbname. Optionally use another user than current user
#
# In psql:
#
# # \l
#
# List all databases on the server, their owners, and user access levels
#
# # \c <dbname>
#
# Connect to a database named
#
# # \dt
#
# Show database tables
#
# # \d <tablename>
#
# Describe table schema
#
# # \q
#
# Quit psql, return to the terminal
#
# # \?
#
# Get help, see list of available commands

# Correct! The IP address 127.0.0.1, also given the shortname localhost, refers to the location of your local machine
# and is the default.

# Takeaways
# We will sometimes want to interact with our database and use its results in a specific programming language. E.g. to
# build web applications or data pipelines in a specific language (Ruby, Python, Javascript, etc.). That's where DBAPIs
# come in.
#
# A DBAPI
# provides a standard interface for one programming language (like Python) to talk to a relational database server.
# Is a low level library for writing SQL statements that connect to a database
# is also known as database adapters
# Different DBAPIs exist for every server framework or language + database system
# Database adapters define a standard for using a database (with SQL) and using the results of database queries as input
# data in the given language.
# Turn a selected SELECT * from some_table; list of rows into an array of objects in Javascript for say a NodeJS adapter;
# or a list of tuples in Python for a Python adapter.
# Examples across languages and server frameworks
# For Ruby (e.g. for Sinatra, Ruby on Rails): pg
# For NodeJS: node-postgres
# For Python (e.g. for Flask, Django): pyscopg2
# psycopg2 is the focus of this course since we are using a Python stack.

# That's right.
# Now that you know Flask, Postgres, and psycopg2, you can now create a database-backed web application without learning
# anything else! You can just send SQL statements directly to the Postgres server from your web server, written in
# Python, and be set to go!
#
# But should we...?
# Writing SQL directly is a fairly clunky way of doing web development. It's useful to learn some higher level libraries
# that let us interact with a database, using Python classes and expressions. Let's get to learn one of the most powerful
# Python libraries for interacting with databases: SQLAlchemy.
#
# Steps for getting a database-backed web application up and running
# Here is an overview of the list of tasks we'll need to do for a given web app to run with a database.
#
# 1. Create a database
# Using createdb in Postgres.
#
# 2. Establish a connection to the database
# We can connect to a Postgres server from a Python web server using pyscopg2 with psycopg2.connect().
#
# 3. Define and create your data schema
# Execute CREATE TABLE commands to create the tables and define the schema (attributes, data types, etc) that will
# define what data gets housed for our web app.
#
# 4. Seed the database with initial data
# (Optional) Give the database some initial data, e.g. test data for doing local development.
#
# 5. Create routes and views
# Create routes in our server that will serve pages (views) to the client. Write up our HTML, CSS, and Javascript
# in our views.
#
# Then finally, to get our web app running,
#
# 6. Run the server
# Get the web server running.
#
# 7. Deploy the server to the web.
# ... and that is, generally, how we would build a web application backed by a database.




