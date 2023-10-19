import { ReactNode } from "react";

type SubSectionLayoutProps = {
    title: string,
    children?: ReactNode,
}

function SubSectionLayout(props: SubSectionLayoutProps) {
    const { title, children } = props;
    return (
        <div className="flex flex-col w-full items-start">
            <div className="bg-[#D9D9D9] py-1 px-4 text-white font-bold text-[16px] w-full flex justify-start">
                {title}
            </div>
            <div className="border-[1px] border-black p-4 w-full space-y-2">
                {
                    children
                }
            </div>
        </div>
    )
}

export default SubSectionLayout;