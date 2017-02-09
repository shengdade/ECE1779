from flask import render_template, redirect, url_for

from app import webapp


@webapp.route('/s3_examples', methods=['GET'])
# Display an HTML list of all s3 buckets.
def s3_list():
    return render_template("s3_examples/list.html", title="S3 Buckets", buckets=buckets)


@webapp.route('/s3_examples/<id>', methods=['GET'])
# Display details about a specific bucket.
def s3_view(id):
    return render_template("s3_examples/view.html", title="S3 Bucket Contents", id=id, keys=keys)


@webapp.route('/s3_examples/upload/<id>', methods=['POST'])
# Upload a new file to an existing bucket
def s3_upload(id):
    return redirect(url_for('s3_view', id=id))
