# EC2 Capacity and Availability
SV328: Enhancing observability in Amazon ECS.

## EC2 Basics

[Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)

## On Demand
* On-demand provisioning
* Variable usage
* Maximum Flexibility
You can spin up and down availabiity as you need it. There are AWS Local Zones as well.

Most common Use Case:
* Cyclical usage
* temp or short tem workloads
* steady state

The elasticity is the benefit here.

On demand is built upon a shared capacity so you may not have that availabiity. Flexibility further improves your availability.

Flexibility
* Instance family (Cs, ms, rs)
* Instance size
* Generation
* CPU Manufacturerzx

EC2 Fleet
* If you are doing a run instance call how do you tell AWS what flexibility you have.

EC2 Autoscaling

You can specify price or capacity optimized instances.

## On Demand Capacity Reservation
* REserved Capcity
* Steady State
* Higher availability

## Capacity Blocks
* Machine Learning instances
* Timebound

## EC2 Spots
* Excess EC2 supply
* If you have a price there is available ec2 spot instances

## EC2 Usage Models

New features allow you to share capacity across AWS accounts.
