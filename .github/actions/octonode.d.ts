declare module "octonode" {

  export function client(accessToken: string): Client

  export class Client {
    public getAsync(path: `/repos/${string}/labels`, params: { page: number, per_page: number }): Promise<[number, [Label]]>
  }

  export interface Label {
    name: string;
    description: string;
    color: string;
  }

}
