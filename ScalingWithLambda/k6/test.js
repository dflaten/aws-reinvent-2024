import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 10,
  duration: "30s",
};

export default function () {
  const response = http.get("http://test.k6.io");
  check(response, {
    "is status 200": (r) => r.status === 200,
  });
  sleep(1);
}
