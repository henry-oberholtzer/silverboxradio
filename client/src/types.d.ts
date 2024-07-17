interface TimestampMixin {
  created: string,
  updated?: string,
}

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

interface InviteSchema extends TimestampMixin {
  id: number,
  email: number,
  owner: UserSchema,
}
