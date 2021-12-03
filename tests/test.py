import time
import requests

test_cases = [
    {
        "sentiment": "FAKE",
        "text": "Nasa is installing internet on the moon"
    },
    {
        "sentiment": "REAL",
        "text": "Guys are stronger than girls"
    },
    {
        "sentiment": "REAL",
        "text": "A university banned the use of capital letters to avoid scaring students"
    },
    {
        "sentiment": "FAKE",
        "text": "Couple in California name baby with emoji"
    }
]

api_url = "http://fakenewssentiment-env.eba-2cfgm4iu.us-east-2.elasticbeanstalk.com/"

def run_test(text):
    headers = {
        "Content-Type" : "application/json"
    }

    start = time.time()
    for i in range(100):
        endpoint = api_url + text
        response = requests.request("GET", endpoint, headers=headers)
        response_json = response.json()
        
    time_passed = time.time() - start
    avg_time_passed = time_passed/100

    return response_json, avg_time_passed


def run_tests():
    for i in range(len(test_cases)):
        print("Running test case: ", i)
        print("Test Input: " + test_cases[i]["text"])
        result, avg_time_passed = run_test(test_cases[i]["text"])
        print("Expected Sentiment: " + test_cases[i]["sentiment"] + " Actual Sentiment: " + result)
        print("Average Latency For 100 Requests: " + str(avg_time_passed))


if __name__ == "__main__":
    run_tests()