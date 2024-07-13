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

interface InvitePostSchema {
  email: string,
}

interface InviteSchema {
  id: number,
  email: number,
  created: string,
  updated?: string,
  owner: UserSchema,
}
