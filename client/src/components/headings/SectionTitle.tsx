import { HTMLProps, ReactNode } from "react";

type SectionTitleProps = {
    children: ReactNode,
    fontSize?: number,
}
    & HTMLProps<HTMLSpanElement>

export default function SectionTitle(props: SectionTitleProps) {
    const { fontSize, children } = props;
    return (
        <span className={`text-[${fontSize ?? 24}px] font-semibold text-black`}>
            {children}
        </span>
    );
}