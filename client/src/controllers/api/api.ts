import { Axios, AxiosRequestConfig } from "axios";

class API {
    private baseURL: string;
    private api: Axios;
    constructor(baseURL: string) {
        this.baseURL = baseURL;
        this.api = new Axios({ baseURL: this.baseURL });
    }
    public async get(url: string, options?: AxiosRequestConfig) {
        const respond = await this.api.get(url, options);
        return respond;
    }
    public async post(url: string, options?: AxiosRequestConfig) {
        const respond = await this.api.post(url, options);
        return respond;
    }
}
export default API;