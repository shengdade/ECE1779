from datetime import datetime, timedelta
from operator import itemgetter

import boto3
from flask import render_template, redirect, url_for

from app import webapp


@webapp.route('/ec2_examples', methods=['GET'])
# Display an HTML list of all ec2 instances
def ec2_list():
    return render_template("ec2_examples/list.html", title="EC2 Instances", instances=instances)


@webapp.route('/ec2_examples/<id>', methods=['GET'])
# Display details about a specific instance.
def ec2_view(id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(id)
    client = boto3.client('cloudwatch')
    metric_name = 'CPUUtilization'  ##    CPUUtilization, NetworkIn, NetworkOut, NetworkPacketsIn,
    #    NetworkPacketsOut, DiskWriteBytes, DiskReadBytes  .....

    namespace = 'AWS/EC2'
    statistic = 'Average'  # could be Sum,Maximum,Minimum,SampleCount,Average
    cpu = client.get_metric_statistics(
        Period=1 * 60,
        StartTime=datetime.utcnow() - timedelta(seconds=60 * 60),
        EndTime=datetime.utcnow() - timedelta(seconds=0 * 60),
        MetricName=metric_name,
        Namespace=namespace,  # Unit='Percent',
        Statistics=[statistic],
        Dimensions=[{'Name': 'InstanceId', 'Value': id}]
    )
    cpu_stats = []
    for point in cpu['Datapoints']:
        hour = point['Timestamp'].hour
        minute = point['Timestamp'].minute
        cpu_stats.append([hour + minute / 60, point['Average']])
    cpu_stats = sorted(cpu_stats, key=itemgetter(0))

    network_in = {}

    net_in_stats = []
    for point in network_in['Datapoints']:
        hour = point['Timestamp'].hour
        minute = point['Timestamp'].minute
        net_in_stats.append([hour + minute / 60, point['Sum']])
    net_in_stats = sorted(net_in_stats, key=itemgetter(0))

    return render_template("ec2_examples/view.html", title="Instance Info",
                           instance=instance, cpu_stats=cpu_stats, net_in_stats=net_in_stats)


@webapp.route('/ec2_examples/create', methods=['POST'])
# Start a new EC2 instance
def ec2_create():
    return redirect(url_for('ec2_list'))


@webapp.route('/ec2_examples/delete/<id>', methods=['POST'])
# Terminate a EC2 instance
def ec2_destroy(id):
    return redirect(url_for('ec2_list'))
