class Solution:
    def simplifyPath(self, path: str) -> str:
        """Simplifies a given absolute path of a Unix file system by removing redundant elements.

        Args:
            path (str): The absolute path of a Unix file system.

        Returns:
            str: The simplified path without unnecessary components (extra slashes, commands: "..", ".")
        """

        stack = []

        for dir_name in path.split("/"):
            if dir_name == "..":
                if stack:
                    stack.pop()
            elif dir_name == "." or dir_name == "":
                continue
            else:
                stack.append(dir_name)

        return "/" + "/".join(stack)
