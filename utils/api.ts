import { loginType, userType } from "./types";

export async function apiRegisterUser(credentials: userType) {
  console.log("", process.env.API_ENDPOINT);

  const response = await fetch(`${process.env.API_ENDPOINT}/register`, {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  return response.json();
}

export async function apiLoginUser(credentials: loginType) {
  console.log("", process.env.API_ENDPOINT);

  const response = await fetch(`${process.env.API_ENDPOINT}/login`, {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(credentials),
  });

  return response.json();
}
