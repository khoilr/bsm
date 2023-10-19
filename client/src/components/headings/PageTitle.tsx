import { HTMLProps, ReactNode } from "react";

export default function PageTitle(props: { children: ReactNode } & HTMLProps<HTMLHeadingElement>) {
    const { children, ...rest } = props;
    return (
        <h2 className="m-0 text-4xl">{props.children}</h2>
    )
}