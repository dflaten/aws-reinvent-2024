import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  scenarios: {
    distributed_scenario: {
      executor: "ramping-vus",
      startVUs: 0,
      stages: [
        { duration: "2m", target: 100 },
        { duration: "5m", target: 100 },
        { duration: "2m", target: 0 },
      ],
      gracefulRampDown: "30s",
    },
  },
  thresholds: {
    http_req_duration: ["p(95)<500"],
    http_req_failed: ["rate<0.01"],
  },
};

const API_URL = __ENV.API_URL;

export default function () {
  const payload = JSON.stringify({
    message: "Hello Python Lambda",
  });

  const params = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = http.post(API_URL, payload, params);

  check(response, {
    "is status 200": (r) => r.status === 200,
    "response time < 500ms": (r) => r.timings.duration < 500,
    "has correct message": (r) =>
      JSON.parse(r.body).message === "Hello from Python Lambda!",
  });

  sleep(1);
}
