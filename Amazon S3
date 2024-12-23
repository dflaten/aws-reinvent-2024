# Dive Deep on Amazon S3

How does the large scale help or make S3 better?

## Physics of Data
**Harddrives**

HDDs have an actuator which reads the spindle (kinda like a record player). Two things need to happen:
1) The arm needs to move into place (seeking, measured in seek time)
2) The disk which is rotating needs to get to the right place (spin time). 
This is the physical limitation of hard drive reading/writing. 

![Hard Drive](https://animagraffs.com/wp-content/uploads/how-hard-disk-drives-work-1.png)
by [Animagraffs](https://animagraffs.com/hard-disk-drive/#embed-code)

**Replication**
The data sent to s3 is stored across multiple shards. This software is called Shardstone. They are stored in a LSM tree in shards. 

Writes - are within control of the software. 
Rights - Not controllable by s3 as customers need to tell you when they want to see the data. 

**Individual Workloads**
They are bursty. They need to be provisioned to handle peak load.

Use Case:
FINRA - Ingests hundreds of billions of records each day with a strict 4 hour window in which it must be processed. 

The large amount of reads that need to be made causes a 100X in capacity over writing. Taken across all of s3 though these peaks even out and the workloads become more stable.

### Theormodynamics: Balancing the aggregates

Overtime data tends to become more cold. The traffic should be balanced across the drives so 
I/O is not left on the table. S3 constantly moves data arround to keep them balanced. When new storage racks are added.

New racks are filled in with existing data instead of just obsorbing new traffic. 

## Designing decorrelated systems
Assigning buckets to their storrage. 
**Simple Solution**
* Assign a user a physical drive for their bucket and put/get your bucket from there.
*Problems*
* you need a backup so you have to go to more than one drive.
* Your storage however now is tied to your physical hardware if you are large enought to have your own drive. 
* If you are small you have to share your drive with others. 

**Shuffle Sharding**
* You purposefully move someones data into different drives, you don't allow them to be correlated. 
* Elastic means any s3 cusomer shold be able to use every drive in our fleet on demand. 
* Its not just drives that shuffle shards, the DNS of putting/get requests are sent to different servers for processing. 
* * POWER OF TWO*If you have a list of drives which have a level of fullness pick two random drives and use the better of the two. 
  
Shuffle Sharding on the AWS builders library has more information on this. 

## Engineering for failure is engineering for velocity
At scale, failures are a fact of life.

How do you know if a system has failed? - S3 is constantly scanning the drives to make sure data is still intact. There are alarms which go off if bytes are not being scanned for too long of a time. 

### Erasure coding. 

Replication is a imple way to tolerate faults - both individual drives and entire Availability Zones. 
This however requires multiple copies which means something takes a ridiculous amount of memory to store. 

Erasure coding uses math to split the object into shards and create extra parity shards; the object can be rebuilt from any K of the shards. 

Any 5 of these shards is enough to rebuild the object, with only 1.8x overhead.
