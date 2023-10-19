import React from "react";

type ContentLayoutProps = {
    children: React.ReactNode,
}

function ContentLayout(props: ContentLayoutProps) {
    return (
        <div className="flex flex-col justify-start items-start p-4 space-y-2 h-full ">
            {props.children}
        </div>
    )
}

export default ContentLayout;