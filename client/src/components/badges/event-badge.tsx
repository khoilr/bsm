import { Badge, BadgeProps } from "@chakra-ui/react";
import { ReactNode } from "react";

type EventBadgeProps = {
    children?: ReactNode,
    bgColor?: string,
} & BadgeProps

function EventBadge(props: EventBadgeProps) {
    const { children, bgColor } = props;
    return (
        <Badge color={bgColor} colorScheme="" padding={4} borderRadius={6}>{children}</Badge>
    )
}

export default EventBadge;