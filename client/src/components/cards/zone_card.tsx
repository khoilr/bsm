import { Button, Card, CardBody, Heading } from "@chakra-ui/react";

type ZoneCardProps = {
    name?: string,
    onTap?: () => void,
}

function ZoneCard(props: ZoneCardProps) {
    return (
        <Card width={250} onClick={props.onTap}>
            <CardBody>
                <img className="w-full h-[150px] object-cover m-0 " src='/images/zone_placeholder.png' />
                <div className="w-full h-[1px] bg-gray-200 my-2"></div>
                <div className="flex justify-between items-center">
                    <Heading size={'sm'} margin={0} textAlign={'left'}>{props.name}</Heading>
                    <Button colorScheme="blue" size={'sm'} onClick={props.onTap}>Detail</Button>
                </div>
            </CardBody>
        </Card>
    )
}

export default ZoneCard;