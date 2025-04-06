# jobicy_data.py

response = {
    'apiVersion': '2.0',
    'documentationUrl': 'https://jobi.cy/apidocs',
    'friendlyNotice': "We appreciate your use of Jobicy API in your projects! Please note that our API access is designed primarily to facilitate broader distribution of our content. We kindly request that you refrain from distributing Jobicy's job listings to any external job platforms, such as Jooble, Google Jobs, and LinkedIn, among others. To ensure that Jobicy is credited as the original source across various platforms, content in the feeds is published with a slight delay. As our data doesn't change frequently, accessing the Feed a few times daily is sufficient and recommended. Be advised that excessive querying may lead to restricted access. Thank you for understanding and cooperating!",
    'jobCount': 6,
    'xRayHash': 'ac90d4ab958aa0925987872dc4abcd52',
    'clientKey': 'a379b5aa59c89858cc4ca2e05041d6ad1ab5d118619785bd3dae12c15ca056f6',
    'lastUpdate': '2025-03-19 05:28:46',
    'jobs': [
        {
            'id': 111598,
            'url': 'https://jobicy.com/jobs/111598-growth-manager-3',
            'jobTitle': 'Growth Manager',
            'companyName': 'Awesome Motive',
            'jobIndustry': ['Marketing & Sales'],
            'jobType': ['full-time'],
            'jobGeo': 'Anywhere',
            'jobLevel': 'Any',
            'jobExcerpt': 'We are Awesome Motive, the company behind popular web apps and business tools...',
            'jobDescription': 'We are Awesome Motive, the company behind popular web apps...',
            'pubDate': '2025-03-19 05:15:32'
        },
        {
            'id': 116374,
            'url': 'https://jobicy.com/jobs/116374-senior-content-marketing-manager-2',
            'jobTitle': 'Senior Content Marketing Manager',
            'companyName': 'Postman',
            'jobIndustry': ['Content & Editorial', 'Marketing & Sales'],
            'jobType': ['full-time'],
            'jobGeo': 'USA',
            'jobLevel': 'Senior',
            'jobExcerpt': 'We’re seeking a creative strategist who’s versed in every aspect of a content marketing ecosystem...',
            'jobDescription': 'We’re seeking a creative strategist who’s versed in every aspect of a content marketing ecosystem...',
            'pubDate': '2025-03-18 16:13:07'
        },
    ]
}


def get_jobs():
    return response['jobs']