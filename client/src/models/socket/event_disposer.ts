
type EventDisposer = {
    name: string,
    listener: (...args: any[]) => void,
}
export default EventDisposer;