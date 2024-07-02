interface UserLoginSchema {
  username: string,
  password: string,
}

interface UserSchema {
  id: number,
  username: string,
  is_admin: boolean,
  email: string,
}
