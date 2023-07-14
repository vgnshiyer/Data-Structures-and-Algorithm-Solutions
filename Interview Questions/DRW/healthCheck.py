'''
Health-checking is a name for ensuring that given network service is responsive & alive. This approach is used for issues detection, warnings about failures or even automated restarts. The task here is to implement a function that will be checking status of few net services. Each of those services has an endpoint /status that can be queried against using HTTP protocol. There is no service that utilizes HTTPS - every one uses plain
HTTP
Implement a function that is to perform health checking for a given list of service addresses. The latter is a string with a valid domain name with port, e.g. localhost:8000. You can use the following libraries:
• asyncio
• aiohttp
A service is considered to be healthy if it responds to a health check request in no longer than 0.5 second and HTTP code will be equal to 200
OK. In case service fails to respond within 0.5 second or HTTP code of response is not 200 OK, the service is to be considered unhealthy.
Requests should be sent using GET method.
The function is expected to return a dictionary where service address (as given in the argument) is a key and value is either True if service is healthy or False otherwise.

Example:
result = await health_check(['localhost: 8000'])
print(result) # {'localhost: 8000': True}

'''

import asyncio

import aiohttp

## reference: https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
async def check_service_health(session, address):
    try:
        async with session.get(f'http://{address}/status', timeout=0.5) as resp:
            if resp.status == 200:
                return True
            else:
                return False
    except:
        return False

async def health_check(services_addresses):
    result = {}

    async with aiohttp.ClientSession() as session:
        tasks = []
        for address in services_addresses:
            task = asyncio.ensure_future(check_service_health(session, address))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        for i in range(len(services_addresses)):
            result[services_addresses[i]] = responses[i]

    return result
