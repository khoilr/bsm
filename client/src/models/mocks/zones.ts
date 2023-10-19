import Zone from "../zones/zones";

const zones: Zone[] = [
    {
        id: '00001',
        name: 'Zone 1',
        description: 'Zone 1 description',
        setting: {
            event: 'check-in',
            limitPeople: 9999,
            notify: false,
        }
    },
    {
        id: '00002',
        name: 'Zone 2 - Security zone',
        description: 'Zone 2 description',
        setting: {
            event: 'check-in',
            limitPeople: 2,
            notify: true,
        }
    }
];
export default zones;